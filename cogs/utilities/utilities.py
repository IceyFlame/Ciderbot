import discord
import random
from discord.ext import commands
from health_server import HealthServer

class Utilities(commands.Cog):
    """Utility commands and basic bot functions"""

    def __init__(self, bot):
        self.bot = bot
        self.health_server = None

    @commands.Cog.listener()
    async def on_ready(self):
        """Event triggered when bot is ready"""
        print(f'{self.bot.user} has connected to Discord!')
        print(f'Bot is connected to {len(self.bot.guilds)} guild(s)')
        print("Registered commands:",
              [command.name for command in self.bot.commands])

        # Start health check server if not already running
        if not self.health_server:
            self.health_server = HealthServer(self.bot)
            self.health_server.start()

    @commands.command(name='hello', help='Responds with a greeting')
    async def hello(self, ctx):
        """Simple hello command"""
        await ctx.send(f'Hello {ctx.author.mention}!')

    @commands.command(name='ping', help='Returns the bot latency')
    async def ping(self, ctx):
        """Check bot latency"""
        latency = round(self.bot.latency * 1000)
        await ctx.send(f'Pong! {latency}ms')

    @commands.command(
        name='friend',
        help='The Global Umamusume inheritence database',
        aliases=["Friend", "friends", "Friends", "inheritance", "Inheritance"])
    async def friend(self, ctx):
        await ctx.send('https://uma.moe/inheritance')

    @commands.command(name='tierlist',
                      help='The Global Umamusume support card tierlist',
                      aliases=["Tierlist"])
    async def tierlist(self, ctx):
        await ctx.send('https://uma.moe/tierlist')

    @commands.command(name='timeline',
                      help='Global Umamusume release timeline',
                      aliases=["release", "Release", "Timeline"])
    async def timeline(self, ctx):
        await ctx.send('https://uma.moe/timeline')

    @commands.command(name='skills',
                      help='Global Umamusume skills',
                      aliases=["Skills", "skill", "Skill"])
    async def skills(self, ctx):
        await ctx.send('https://gametora.com/umamusume/skills')
        await ctx.send(
            'https://docs.google.com/spreadsheets/u/0/d/1oB3eTvKqREtJDWJL0q80O_VjBcpOmRl5xE0z5fZKgFY/htmlview'
        )

    @commands.command(name='Umapyoi',
                      help='Delivers the link to Umapyoi Densetsu!',
                      aliases=['umapyoi'])
    async def umapyoi(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=jIxarCsmxZ8')

    @commands.command(name='LegendU',
                      help='Delivers the link to Girls Legend U!',
                      aliases=['legendu', 'legendU', 'Legendu'])
    async def legendU(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=_m8_jvN41UM')

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore bot's own messages
        if message.author == self.bot.user:
            return

        # More specific check for "3rd place"
        if self.bot.user.mentioned_in(message):
            content_lower = message.content.lower()

            # Check for exact phrase "3rd place" (case insensitive)
            if "3rd place" in content_lower:
                await message.reply(
                    "https://tenor.com/view/s2-umamusume-pretty-derby-neicha-nice-nature-gif-7369094384855945877"
                )
                return

            elif "3rd" in content_lower:
                await message.reply(
                    "https://tenor.com/view/s2-umamusume-pretty-derby-neicha-nice-nature-gif-7369094384855945877"
                )
                return

            # If you want to add more specific phrases later:
            # elif "another phrase" in content_lower:
            #     await message.reply("Another response")
            #     return

        # Generic Response
        target_user_id = 1328852892731445260
        if any(user.id == target_user_id for user in message.mentions):
            responses = [
                "👋 おいつ！ナイスネイチャです～", "😖 にがい.", "😇 どうぞよろしく～", "🎯 どして？なにが？",
                "😎 よっ！", "😅 はい、はい-", "HARIKITTE IKKOU"
            ]
            response = random.choice(responses).format(
                user=message.author.mention)
            await message.reply(response)


async def setup(bot):
    await bot.add_cog(Utilities(bot))
