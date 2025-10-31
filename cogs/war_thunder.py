import discord
from discord.ext import commands
from discord import app_commands
from .tanks_data import *

class war_thunder(commands.Cog):
    """War Thunder specific commands"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="lineup",
        description="Generate a ground realistic battles lineup for War Thunder"
    )
    @app_commands.describe(
        battle_rating="The battle rating for the lineup (e.g., 5.7, 10.0)",
        nation="Nation to generate lineup for",
        account_type="F2P or P2W vehicles"
    )
    @app_commands.choices(
        nation=[
            app_commands.Choice(name="USA", value="usa"),
            app_commands.Choice(name="Germany", value="germany"),
            app_commands.Choice(name="USSR", value="ussr"),
            app_commands.Choice(name="Great Britain", value="britain"),
            app_commands.Choice(name="Japan", value="japan"),
            app_commands.Choice(name="China", value="china"),
            app_commands.Choice(name="Italy", value="italy"),
            app_commands.Choice(name="France", value="france"),
            app_commands.Choice(name="Sweden", value="sweden"),
            app_commands.Choice(name="Israel", value="israel"),
        ],
        account_type=[
            app_commands.Choice(name="Free to Play", value="f2p"),
            app_commands.Choice(name="Pay to Win", value="p2w"),
        ]
    )
    async def lineup(
        self, 
        interaction: discord.Interaction, 
        battle_rating: str,
        nation: app_commands.Choice[str],
        account_type: app_commands.Choice[str]
    ):
        """Generate a ground RB lineup for the specified parameters"""
        
        # Validate battle rating format
        try:
            br_float = float(battle_rating)
            if br_float < 1.0 or br_float > 12.7:
                await interaction.response.send_message(
                    "❌ Battle rating must be between 1.0 and 12.7", 
                    ephemeral=True
                )
                return
        except ValueError:
            await interaction.response.send_message(
                "❌ Invalid battle rating format. Use decimal format like '5.7' or '10.0'", 
                ephemeral=True
            )
            return

        # Defer the response since database lookup might take time
        await interaction.response.defer()

        try:
            # This is where your logic will go
            lineup_data = await self.generate_lineup(
                br_float, 
                nation.value, 
                account_type.value
            )
            
            # Send the result
            await interaction.followup.send(embed=lineup_data)
            
        except Exception as e:
            await interaction.followup.send(
                f"❌ An error occurred while generating the lineup: {str(e)}"
            )

    async def generate_lineup(
    self, 
    battle_rating: float, 
    nation: str, 
    account_type: str
) -> discord.Embed:
        """Generate the actual lineup"""
        
        # Get vehicles filtered by nation and account type
        all_vehicles = await self.get_vehicles_by_nation(nation, account_type)
        
        # Filter vehicles within acceptable BR range (typically ±1.0)
        br_range_vehicles = [
            v for v in all_vehicles 
            if battle_rating - 1.0 <= v['br'] <= battle_rating + 0.3
        ]
        
        lineup = []
        slots_filled = 0
        total_slots = 7
        
        # Step 1: Find light tank (highest BR light tank available)
        light_tanks = [v for v in br_range_vehicles if v['type'] == 'light_tank']
        if light_tanks:
            light_tank = max(light_tanks, key=lambda x: x['br'])
            lineup.append(light_tank)
            br_range_vehicles.remove(light_tank)
            slots_filled += 1
        
        # Step 2: Find SPAA (highest BR SPAA available)
        spaas = [v for v in br_range_vehicles if v['type'] == 'spaa']
        if spaas:
            spaa = max(spaas, key=lambda x: x['br'])
            lineup.append(spaa)
            br_range_vehicles.remove(spaa)
            slots_filled += 1
        
        # Step 3: Find tank destroyer (highest BR TD available)
        tank_destroyers = [v for v in br_range_vehicles if v['type'] == 'tank_destroyer']
        if tank_destroyers:
            tank_destroyer = max(tank_destroyers, key=lambda x: x['br'])
            lineup.append(tank_destroyer)
            br_range_vehicles.remove(tank_destroyer)
            slots_filled += 1
        
        # Step 4: Find heavy tank (highest BR heavy tank available)
        heavy_tanks = [v for v in br_range_vehicles if v['type'] == 'heavy_tank']
        if heavy_tanks:
            heavy_tank = max(heavy_tanks, key=lambda x: x['br'])
            lineup.append(heavy_tank)
            br_range_vehicles.remove(heavy_tank)
            slots_filled += 1
        
        # Step 5: Fill remaining slots with medium tanks
        # Start with exact BR match, then move down
        medium_tanks = [v for v in br_range_vehicles if v['type'] == 'medium_tank']
        
        # Sort medium tanks by BR (closest to target BR first, then descending)
        medium_tanks.sort(key=lambda x: (abs(x['br'] - battle_rating), -x['br']))
        
        # Fill remaining slots with medium tanks
        remaining_slots = total_slots - slots_filled
        for i in range(min(remaining_slots, len(medium_tanks))):
            lineup.append(medium_tanks[i])
            slots_filled += 1
        
        # If we still have slots, fill with any remaining vehicles (sorted by BR)
        if slots_filled < total_slots:
            remaining_vehicles = [v for v in br_range_vehicles if v not in lineup]
            remaining_vehicles.sort(key=lambda x: x['br'], reverse=True)
            
            for i in range(min(total_slots - slots_filled, len(remaining_vehicles))):
                lineup.append(remaining_vehicles[i])
        
        # Create embed with the lineup
        embed = discord.Embed(
            title=f"{nation.upper()} {battle_rating} {account_type.upper()} Lineup",
            description="Ground Realistic Battles",
            color=discord.Color.blue()
        )
        
        # Format vehicle list
        vehicle_list = []
        for vehicle in lineup:
            premium_indicator = " ⭐" if vehicle.get('premium', False) else ""
            vehicle_list.append(f"• {vehicle['name']} ({vehicle['br']}){premium_indicator}")
        
        embed.add_field(
            name="Lineup Composition",
            value="\n".join(vehicle_list) if vehicle_list else "No vehicles found",
            inline=False
        )
        
        embed.add_field(
            name="Composition Breakdown",
            value=f"Light Tank: {len([v for v in lineup if v['type'] == 'light_tank'])}\n"
                f"SPAA: {len([v for v in lineup if v['type'] == 'spaa'])}\n"
                f"Tank Destroyer: {len([v for v in lineup if v['type'] == 'tank_destroyer'])}\n"
                f"Heavy Tank: {len([v for v in lineup if v['type'] == 'heavy_tank'])}\n"
                f"Medium Tanks: {len([v for v in lineup if v['type'] == 'medium_tank'])}\n"
                f"Other: {len([v for v in lineup if v['type'] not in ['light_tank', 'spaa', 'tank_destroyer', 'heavy_tank', 'medium_tank']])}",
            inline=True
        )
        
        embed.set_footer(text="Lineup generated by War Thunder Bot")
        
        return embed

    async def get_vehicles_by_nation(self, nation: str, account_type: str) -> list:
        """Get vehicles for specified nation and filter by account type"""
        nation_map = {
            'usa': usa_vehicles,
            'germany': germany_vehicles,
            'ussr': ussr_vehicles,
            'britain': britain_vehicles,
            'japan': japan_vehicles,
            'china': china_vehicles,
            'italy': italy_vehicles,
            'france': france_vehicles,
            'sweden': sweden_vehicles,
            'israel': israel_vehicles
        }
        
        vehicles = nation_map.get(nation, [])
        
        if account_type == "f2p":
            return [v for v in vehicles if not v['premium']]
        elif account_type == "p2w":
            return vehicles  # Include all vehicles for P2W
        else:
            return vehicles

    @commands.command(name='research', help='shows research progress in war thunder')
    async def research(self, ctx):
        await ctx.send(f"""When researching vehicles **+/- 1** rank than what you are currently using, you incur a research penalty. This penalty applies to all earned RP with two exceptions.

- Research points gained when finishing a rank of modifications on a vehicle you have used.
- Carryover RP (the RP that you can invest in the next vehicle when you finish a vehicle with more RP than you needed), 
has already had the penalty applied when you earned it, meaning you can invest it into a vehicle of any tier without additional penalties.

Premium vehicles have the special property of being able to research all vehicles of lower tiers with no penalty, in addition to being able to research up to one tier higher like normal vehicles.
This Bonus **DOES NOT** apply to Squadron or Event vehicles, although some event vehicles are premium as well. You can always tell a premium by the golden background in the vehicle selection screen.
This Bonus **DOES NOT** apply to situations in which a tech tree has a full rank worth of a gap, such as the Italian tree's F84F into Tornado (shown below). Playing the previous vehicle in a line *always* gives the added RP bonus.

For the different penalty levels refer to the sheet below. It describes the effective RP earned when playing different tiers.
https://cdn.discordapp.com/attachments/448113238400303115/1179893424502087700/image.png?ex=657b7061&is=6568fb61&hm=7fc1c75213ff8f8fd6f76517ba55aa309694b90fcdf9a2ef01fba26fbe0defaf&
https://cdn.discordapp.com/attachments/580302435147448336/1183502495641776268/image.png?ex=65889197&is=65761c97&hm=52342e65ee7b3373b452dbe04b7b7140e8c6a036b9df741b0f5d807ceb77eaf1&""")

    @commands.command(name='missile_evasion', help='shows steps on missile evasion')
    async def missile_evasion(self, ctx):
        await ctx.send(f"""A few videos by DEFYN on how to evade every missile type (IR, IRCCM, SARH, ARH), as well as a useful diagram explaining how to notch.

# **War Thunder Guide 6.0 - Defeating Infrared Guided Missiles (IRCCM Included)**
<https://www.youtube.com/watch?v=Q4PMaFA9Obs>
# **War Thunder Air Guides Part 7 - Using And Defeating Radar Missiles (FOX-3 & FOX-1)**
<https://www.youtube.com/watch?v=l80IHJPOh9w>
https://media.discordapp.net/attachments/499222683435794432/1253818356654542918/notchDiagram.png?ex=672bda57&is=672a88d7&hm=e0b58cb40157f1a688dc2958f272615f888baf5ba255b80bdaa4efda60566442&format=webp&quality=lossless&width=1819&height=1365&""")

    @commands.command(name='weaponry_data')
    async def weaponry_data(self, ctx):
        await ctx.send(f"""**Stats for almost all guided weapons in game:**
https://docs.google.com/spreadsheets/d/1SsOpw9LAKOs0V5FBnv1VqAlu3OssmX7DJaaVAUREw78/edit#gid=1624345539'""")
        
    


async def setup(bot):
    await bot.add_cog(war_thunder(bot))