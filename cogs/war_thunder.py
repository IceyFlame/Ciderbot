import discord
import random
from discord.ext import commands

class war_thunder(commands.Cog):
    """War Thunder specific commands"""

    def __init__(self, bot):
        self.bot = bot

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

    

async def setup(bot):
    await bot.add_cog(war_thunder(bot))