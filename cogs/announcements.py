import discord
from discord.ext import commands
from discord import app_commands

class announcements(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @app_commands.default_permissions(manage_messages=True)
    @app_commands.checks.has_permissions(manage_messages=True)
    @app_commands.command(name="announce", description="Make an announcement with an embed")
    @app_commands.describe(
        title="The title of the announcement",
        description="The main content of the announcement",
        color="Color for the embed (hex code without #)",
        channel="Channel to send the announcement to (optional)",
        thumbnail="URL for thumbnail image (optional)",
        image="URL for main image (optional)"
    )
    async def announce(
        self,
        interaction: discord.Interaction,
        title: str,
        description: str,
        color: str = None,
        channel: discord.TextChannel = None,
        thumbnail: str = None,
        image: str = None
    ):
        # Default to blue color if none provided
        embed_color = discord.Color.blue()
        if color:
            try:
                # Convert hex color to integer
                embed_color = discord.Color(int(color, 16))
            except ValueError:
                await interaction.response.send_message("Invalid color format! Use hex without # (e.g., FF0000 for red)", ephemeral=True)
                return

        # Create embed
        embed = discord.Embed(
            title=title,
            description=description,
            color=embed_color,
            timestamp=discord.utils.utcnow()
        )

        # Add thumbnail if provided
        if thumbnail:
            embed.set_thumbnail(url=thumbnail)

        # Add image if provided
        if image:
            embed.set_image(url=image)

        # Add footer with author info
        embed.set_footer(text=f"Announcement by {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)

        # Determine target channel
        target_channel = channel or interaction.channel

        try:
            # Send the announcement
            await target_channel.send(embed=embed)
            
            # Confirm to the user
            await interaction.response.send_message(
                f"✅ Announcement sent to {target_channel.mention}!",
                ephemeral=True
            )
        except discord.Forbidden:
            await interaction.response.send_message("❌ I don't have permission to send messages in that channel!", ephemeral=True)
        except discord.HTTPException as e:
            await interaction.response.send_message(f"❌ Failed to send announcement: {e}", ephemeral=True)

    # Optional: Add a simpler version with just title and description
    @app_commands.default_permissions(manage_messages=True)
    @app_commands.checks.has_permissions(manage_messages=True)
    @app_commands.command(name="quickannounce", description="Make a quick announcement")
    @app_commands.describe(
        title="The title of the announcement",
        message="The announcement message"
    )
    async def quickannounce(self, interaction: discord.Interaction, title: str, message: str):
        embed = discord.Embed(
            title=title,
            description=message,
            color=discord.Color.green(),
            timestamp=discord.utils.utcnow()
        )
        embed.set_footer(text=f"Announced by {interaction.user.display_name}")

        await interaction.response.send_message("✅ Quick announcement sent!", ephemeral=True)
        await interaction.channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(announcements(bot))