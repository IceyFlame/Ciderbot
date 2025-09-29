import discord
import datetime
from discord.ext import commands
from discord import app_commands

class Moderation(commands.Cog):
    """Moderation commands for server management"""
    
    def __init__(self, bot):
        self.bot = bot
    
    # Timeout (Temporary Mute) Command
    @app_commands.command(name="timeout", description="Timeout a member for a specified duration")
    @app_commands.describe(
        member="The member to timeout",
        duration="Duration in minutes",
        reason="Reason for the timeout (optional)"
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def timeout(self, interaction: discord.Interaction, member: discord.Member, duration: int, reason: str = "No reason provided"):
        """Timeout a member for a specified duration"""
        if member.guild_permissions.administrator:
            await interaction.response.send_message("❌ Cannot timeout an administrator!", ephemeral=True)
            return
        
        if duration <= 0:
            await interaction.response.send_message("❌ Duration must be positive!", ephemeral=True)
            return
        
        # Maximum timeout duration is 28 days (40320 minutes)
        if duration > 40320:
            await interaction.response.send_message("❌ Maximum timeout duration is 28 days!", ephemeral=True)
            return
        
        timeout_duration = datetime.timedelta(minutes=duration)
        
        try:
            await member.timeout(timeout_duration, reason=reason)
            await interaction.response.send_message(
                f"✅ {member.mention} has been timed out for {duration} minutes.\nReason: {reason}",
                ephemeral=False
            )
        except discord.Forbidden:
            await interaction.response.send_message("❌ I don't have permission to timeout this member!", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ An error occurred: {e}", ephemeral=True)

    # Remove Timeout Command
    @app_commands.command(name="untimeout", description="Remove timeout from a member")
    @app_commands.describe(
        member="The member to remove timeout from",
        reason="Reason for removing timeout (optional)"
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def untimeout(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
        """Remove timeout from a member"""
        # Check if member is timed out by looking at timed_out_until
        if member.timed_out_until is None:
            await interaction.response.send_message("❌ This member is not timed out!", ephemeral=True)
            return
        
        try:
            await member.timeout(None, reason=reason)
            await interaction.response.send_message(
                f"✅ Timeout removed from {member.mention}.\nReason: {reason}",
                ephemeral=False
            )
        except discord.Forbidden:
            await interaction.response.send_message("❌ I don't have permission to remove timeout from this member!", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ An error occurred: {e}", ephemeral=True)

    # Kick Command
    @app_commands.command(name="kick", description="Kick a member from the server")
    @app_commands.describe(
        member="The member to kick",
        reason="Reason for the kick (optional)"
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
        """Kick a member from the server"""
        if member.guild_permissions.administrator:
            await interaction.response.send_message("❌ Cannot kick an administrator!", ephemeral=True)
            return
        
        if member == interaction.user:
            await interaction.response.send_message("❌ You cannot kick yourself!", ephemeral=True)
            return
        
        try:
            await member.kick(reason=reason)
            await interaction.response.send_message(
                f"✅ {member.mention} has been kicked from the server.\nReason: {reason}",
                ephemeral=False
            )
        except discord.Forbidden:
            await interaction.response.send_message("❌ I don't have permission to kick this member!", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ An error occurred: {e}", ephemeral=True)

    # Ban Command
    @app_commands.command(name="ban", description="Ban a member from the server")
    @app_commands.describe(
        member="The member to ban",
        reason="Reason for the ban (optional)",
        delete_message_days="Number of days of messages to delete (0-7)"
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided", delete_message_days: int = 0):
        """Ban a member from the server"""
        if member.guild_permissions.administrator:
            await interaction.response.send_message("❌ Cannot ban an administrator!", ephemeral=True)
            return
        
        if member == interaction.user:
            await interaction.response.send_message("❌ You cannot ban yourself!", ephemeral=True)
            return
        
        # Validate delete_message_days
        delete_message_days = max(0, min(7, delete_message_days))
        
        try:
            await member.ban(reason=reason, delete_message_days=delete_message_days)
            await interaction.response.send_message(
                f"✅ {member.mention} has been banned from the server.\n"
                f"Reason: {reason}\n"
                f"Messages deleted: {delete_message_days} days",
                ephemeral=False
            )
        except discord.Forbidden:
            await interaction.response.send_message("❌ I don't have permission to ban this member!", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ An error occurred: {e}", ephemeral=True)

    # Help command to show available moderation commands
    @app_commands.command(name="modhelp", description="Show moderation command help")
    async def modhelp(self, interaction: discord.Interaction):
        """Show moderation command help"""
        help_text = """
        **Moderation Commands:**
        `/timeout <member> <duration> [reason]` - Timeout a member
        `/untimeout <member> [reason]` - Remove timeout from a member  
        `/kick <member> [reason]` - Kick a member from the server
        `/ban <member> [reason] [delete_days]` - Ban a member from the server
        
        **Required Permissions:**
        - Timeout/Untimeout: Moderate Members
        - Kick: Kick Members  
        - Ban: Ban Members
        """
        await interaction.response.send_message(help_text, ephemeral=True)

    # Error handling for permission checks
    @timeout.error
    @untimeout.error
    @kick.error
    @ban.error
    async def command_error(self, interaction: discord.Interaction, error):
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message("❌ You don't have permission to use this command!", ephemeral=True)
        else:
            await interaction.response.send_message(f"❌ An error occurred: {error}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Moderation(bot))