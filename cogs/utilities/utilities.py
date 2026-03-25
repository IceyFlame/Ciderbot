import discord
import random
from discord.ext import commands

class Utilities(commands.Cog):
    """Utility commands and basic bot functions"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Event triggered when bot is ready"""
        print(f'{self.bot.user} has connected to Discord!')
        print(f'Bot is connected to {len(self.bot.guilds)} guild(s)')
        print("Registered commands:",
              [command.name for command in self.bot.commands])

    @commands.command(name='hello', help='Responds with a greeting')
    async def hello(self, ctx):
        """Simple hello command"""
        await ctx.send(f'Hello {ctx.author.mention}!')

    @commands.command(name = 'Winning Live', help = 'displays the winning live songs for each scenario', aliases=["wl"])
    async def wl(self, ctx):
        await ctx.send("""Below is a compilation of Winning Live songs for each scenario (as compiled by CrippleCrownEmperor):

URA Finale - [Umapyoi Densetsu](https://www.youtube.com/watch?v=NaYMw_P4WU8&list=PLBAg4T7zxKzo3p36JbSTBgOjTJcZ0rZ8V&index=5&pp=iAQB8AUB)
Aoharu Hai (Unity Cup) - [WINnin' Five](https://www.youtube.com/watch?v=mR01PgKF-lU&list=PLBAg4T7zxKzo3p36JbSTBgOjTJcZ0rZ8V&index=10&pp=iAQB8AUB)
Make a New Track (Trackblazer) - [Blow my Gale](https://www.youtube.com/watch?v=7OuVm8V122Q&list=PLBAg4T7zxKzo3p36JbSTBgOjTJcZ0rZ8V&index=17&pp=iAQB8AUB)
Our Grand Live - [Girls' Legend U](https://www.youtube.com/watch?v=G7RmGsHxv-Q&list=PLBAg4T7zxKzo3p36JbSTBgOjTJcZ0rZ8V&index=1&pp=iAQB8AUB)
Grand Masters - [Everlasting Beats](https://www.youtube.com/watch?v=wq0S1dbTWio&list=PLBAg4T7zxKzo3p36JbSTBgOjTJcZ0rZ8V&index=47&pp=iAQB8AUB)
Project l'Arc - [L'Arc de Gloire](https://www.youtube.com/watch?v=GJNMS1jEV_o&list=PLBAg4T7zxKzo3p36JbSTBgOjTJcZ0rZ8V&index=53&pp=iAQB8AUB)
U.A.F. Ready GO! - [Bakunetsu my Soul](https://www.youtube.com/watch?v=AvoWpVmJHgI&list=PLBAg4T7zxKzo3p36JbSTBgOjTJcZ0rZ8V&index=63&pp=iAQB8AUB)
Shuukaku! Manpaku! Daihoushokusa - [Umasugi! Gourmet Parade](https://www.youtube.com/watch?v=c2EerlVb7Js&list=PLBAg4T7zxKzo3p36JbSTBgOjTJcZ0rZ8V&index=74&pp=iAQB8AUB)
Run! Mecha-Umamusume - [O-Rorize](https://www.youtube.com/watch?v=HjMuwuyFkxI&list=RDHjMuwuyFkxI&start_radio=1&pp=ygUIby1yb3JpemWgBwE%3D)
The Twinkle Legends - [Legend Changer](https://www.youtube.com/watch?v=Kpf2mmyzuMM&list=RDKpf2mmyzuMM&start_radio=1&pp=ygUOTGVnZW5kIENoYW5nZXKgBwE%3D)
Design Your Island - [Tucker's Skill-Up Island](https://www.youtube.com/watch?v=Fl-4S-vUxPg&list=RDFl-4S-vUxPg&start_radio=1)
Paradise ♪ Yukoma Hot Springs - [Yukoma Thermae](https://www.youtube.com/watch?v=86I1qlLny_A&list=RD86I1qlLny_A&start_radio=1&pp=ygUOeXVrb21hIHRoZXJtYWWgBwE%3D)
Beyond Dreams - [UMA in America](https://www.youtube.com/watch?v=oQQCBaGO8oU&list=RDoQQCBaGO8oU&start_radio=1)""", suppress_embeds=True)


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
