import discord
import datetime
from discord.ext import commands
from discord import app_commands
from cogs.game_data.cups_data import CM_DATABASE, NEXT_CUP

class cm_info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cm_database = CM_DATABASE
        self.next_cup = NEXT_CUP

    @app_commands.command(name="cm-info", description="Get information about Champions Meet cups")
    @app_commands.describe(cup_name="Select a specific cup or get the next one")
    async def cm_info(self, interaction: discord.Interaction, cup_name: str = None):
        """Display Champions Meet information"""
        
        if cup_name is None:
            # Show next cup
            if self.next_cup in self.cm_database:
                cup = self.cm_database[self.next_cup]
                embed = discord.Embed(
                    title="🏆 NEXT CHAMPIONS MEET",
                    description=f"**{cup.name}**\n{cup.get_formatted_info()}",
                    color=0x00ff00
                )
                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message("❌ Next cup not found in database.", ephemeral=True)
        else:
            # Show specific cup
            cup_key = cup_name.upper()
            if cup_key in self.cm_database:
                cup = self.cm_database[cup_key]
                embed = discord.Embed(
                    title=f"🏆 {cup.name}",
                    description=cup.get_formatted_info(),
                    color=0x0099ff
                )
                await interaction.response.send_message(embed=embed)
            else:
                # Try case-insensitive search
                found_cup_key = None
                for key in self.cm_database:
                    if cup_name.lower() in key.lower():
                        found_cup_key = key
                        break
                
                if found_cup_key:
                    cup = self.cm_database[found_cup_key]
                    embed = discord.Embed(
                        title=f"🏆 {cup.name}",
                        description=cup.get_formatted_info(),
                        color=0x0099ff
                    )
                    await interaction.response.send_message(embed=embed)
                else:
                    available_cups = ", ".join(self.cm_database.keys())
                    await interaction.response.send_message(
                        f"❌ Cup '{cup_name}' not found. Available cups: {available_cups}",
                        ephemeral=True
                    )

    @cm_info.autocomplete('cup_name')
    async def cm_info_autocomplete(self, interaction: discord.Interaction, current: str):
        """Autocomplete for cup names"""
        cups = list(self.cm_database.keys())
        if current:
            # Filter cups that match the current input
            matches = [cup for cup in cups if current.lower() in cup.lower()]
        else:
            matches = cups
        
        # Return top 25 matches as choices
        return [
            app_commands.Choice(name=cup, value=cup)
            for cup in matches[:25]
        ]
    
async def setup(bot):
    await bot.add_cog(cm_info(bot))