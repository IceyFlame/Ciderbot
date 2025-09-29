import discord
import random
import time
from discord.ext import commands
from config import Config

class FunCommands(commands.Cog):
    """Fun and game-related commands"""
    
    def __init__(self, bot):
        self.bot = bot
    
    def process_strings(self, string1, string2, string3, string4):
        """Process gear strings with suffix-based logic"""
        cc = 0
        cd = 0
        s = 0
        
        def parse_value(input_str):
            nonlocal cc, cd, s
            
            # Check if the value has a valid suffix or no suffix at all
            valid_suffixes = ["cc", "cd", "s", "spd"]
            if any(input_str.endswith(suffix) for suffix in valid_suffixes):
                if input_str.endswith("cc") and cc == 1:
                    raise ValueError(f"Duplicate suffixes in{input_str}")
                if input_str.endswith("cc"):
                    cc = 1
                    return float(input_str[:-2]) * 1.6
                if input_str.endswith("cd") and cd == 1:
                    raise ValueError(f"Duplicate suffixes in{input_str}")
                elif input_str.endswith("cd"):
                    cd = 1
                    return float(input_str[:-2]) * 1.1
                if (input_str.endswith("s") or input_str.endswith("spd")) and s == 1:
                    raise ValueError(f"Duplicate suffixes in{input_str}")
                elif (input_str.endswith("s")):
                    s = 1
                    return float(input_str[:-1]) * 2
                elif (input_str.endswith("spd")):
                    s = 1
                    return float(input_str[:-3]) * 2
            elif input_str.isdigit():  # Handle values without a suffix
                return float(input_str)
            else:
                raise ValueError(f"Invalid input: '{input_str}'")

        # Parse and sum the values
        parsed_values = []
        for value in [string1, string2, string3, string4]:
            parsed_val = parse_value(value)
            if parsed_val is not None:
                parsed_values.append(parsed_val)
        
        total = sum(parsed_values)
        strings = [string1, string2, string3, string4]
        
        speedValue = 0
        for s in strings:
            try:
                if (s.endswith("s")):
                    speedValue = float(s[:-1])
                elif(s.endswith("spd")):
                    speedValue = float(s[:-3])
                else:
                    continue
            except ValueError:
                continue
        
        total = round(total, 1)
        rand = random.random()
        if (speedValue >= 25):
            responses = [
                f"This piece of gear is... {total}gs. Wait, what's this? a Speed Badge gear? Well, I certainly didn't expect that.",
                f"This piece of gear is... {total}gs. Huh? Wait, it's a Speed Badge Gear! How magnificent!",
                f"This piece of gear is... {total}gs. A Speed Badge gear too! Well, that certainly exceeded my expectations.",
                f"This piece of gear is... {total}gs. Oh, it's a Speed Badge gear! Saving this piece for the Barry Allen cosplay, are we?",
                f"This piece of gear is... {total}gs. A speed Badge gear, huh. Looks like someone's spending money on this game..."
            ]
            return responses[int(rand * 5)]
            
        if (total > 75):
            responses = [
                f"This piece of gear is... {total}gs. Ara~",
                f"This piece of gear is... {total}gs. *gasp* you've finally made your ancestors proud!",
                f"This piece of gear is... {total}gs. goodness me, how splendid!",
                f"This piece of gear is... {total}gs. What an exemplary specimen! It's... breathtaking.",
                f"This piece of gear is... {total}gs. Well... I haven't seen many better than this, that's for sure!"
            ]
            return responses[int(rand * 5)]
        elif (total > 70):
            responses = [
                f"This piece of gear is {total}gs. great work!",
                f"This piece of gear is {total}gs. did you lucksack or was it all planned?",
                f"This piece of gear is {total}gs. as every piece of gear should be.",
                f"This piece of gear is {total}gs. c'mere, you get a hug.",
                f"This piece of gear is {total}gs. maybe I was too harsh with you."
            ]
            return responses[int(rand * 5)]
        elif (total > 60):
            responses = [
                f"This piece of gear is {total}gs. I would give it a B, for being so barely average.",
                f"This piece of gear is {total}gs. it better be a right side piece or I'm coming for your throat.",
                f"This piece of gear is {total}gs. you couldn't have rolled this a little higher now?",
                f"This piece of gear is {total}gs. Allowing yourself to be satisfied by mediocrity like this leads only to failure.",
                f"This piece of gear is {total}gs. Eh... this isn't the worst shit I've seen."
            ]
            return responses[int(rand * 5)]
        elif (total > 50):
            responses = [
                f"This piece of gear is {total}gs. I'd give that a D, for \"Damn, did you get dropped on your head as a kid?\"",
                f"This piece of gear is {total}gs. I wouldn't feed the dogs this slop.",
                f"This piece of gear is {total}gs. where did you find this, a fucking walmart dumpster?",
                f"This piece of gear is {total}gs. I would rather die than look at any of this shit ever again.",
                f"This piece of gear is {total}gs. Apologize for being born into this world, I have no clue how natural selection missed you."
            ]
            return responses[int(rand * 5)]
        else:
            return f"This piece of gear is {total}gs. Find a garbage chute, get rid of it, remove yourself from the gene pool too while you're at it."

    @commands.command(name="gs")
    async def gs_command(self, ctx, *args):
        """Command to process four strings for gear scoring"""
        if len(args) != 4:
            await ctx.send("That's not how you use the command, dummy. use ?gshelp for instructions, or try again.")
            return
        
        try:
            result = self.process_strings(*args)
            await ctx.send(result)
        except Exception:
            await ctx.send("That's not how you use the command, dummy. Let's try again.")

    @commands.command(name="gshelp")
    async def gshelp_command(self, ctx): 
        await ctx.send("Usage: ?gs <a> <b> <c> <d>. all four values must be integers, or ending with cc, cd and s/spd. no duplicate suffixes should be used. convert flat stats into % by dividing by the unit's base stat then multiplying by 100, and round to the nearest integer.")
    
    @commands.command(name="wukong")
    async def wukong_command(self, ctx):
        await ctx.send("https://tenor.com/view/smelling-monkey-zoo-lol-gif-4050322")

    def sim_pull(self, num):
        """Simulate a moonlight pull"""
        threeStar = ["Camilla", "Rikoris", "Gunther", "Arowell", "Eaton", "Yoonryong", "Mirsa", "Talia", "Celeste", "Gloomyrain", "Doris", "Elson", "Sonia", "Batisse", "Church of Illryos Axe", "Lorina", "Pernilla", "Hasol", "Pyllis", "Penelope", "Revna", "Sven", "Wanda", "Hurado", "Otillie", "Suthan", "Ainos", "Requiemroar"]
        fourStar = ["New Kid Adin", "General Purrgis", "Crimson Armin", "Fighter Maya", "Last Piece Karin", "Tempest Surin", "Wanderer Silk", "Watcher Schuri", "Angel of Light Angelica", "Benevolent Romann", "Guider Aither", "Wandering Prince Cidd", "Blaze Dingo", "Infinite Horizon Achates", "Moon Bunny Dominiel", "Assassin Cartuja", "Bad Cat Armin", "Great Chief Khawana", "Inferno Khawazu", "Kitty Clarissa", "Shadow Rose", "Troublemaker Crozet", "Assassin Cidd", "Assassin Coli", "Blood Blade Karin", "Crescent Moon Rin", "Peacemaker Furious", "Roaming Warrior Leo", "Westwind Executioner Schuri", "Auxiliary Lots", "Celestial Mercedes", "Challenger Dominiel", "Champion Zerato", "Shooting Star Achates", "Sinful Angelica", "Mario", "Sonic the Hedgehog"]
        fiveStar = ["Conqueror Lilias", "Judge Kise", "Lionheart Cermia", "Little Queen Charlotte", "Ambitious Tywin", "Belian", "Dragon Bride Senya", "Empyrean Ilynav", "Last Rider Krau", "Navy Captain Landy", "Specimen Sez", "Spirit Eye Celine", "Twisted Eidolon Kayron", "Astromancer Elena", "Commander Pavel", "Faithless Lidica", "Architect Laika", "New Moon Luna", "Sage Baal and Sezan", "Silver Blade Aramintha", "Solitaria of the Snow", "Sylvan Sage Vivian", "Desert Jewel Basar", "Dragon King Sharun", "Maid Chloe", "Ruele of Light", "Apocalypse Ravi", "Bystander Hwayoung", "Dark Corvus", "Designer Lilibet", "Lone Crescent Bellona", "Martial Artist Ken", "Mediator Kawerik", "Straze", "Urban Shadow Choux", "Abyssal Yufine", "Fallen Cecilia", "Arbiter Vildred", "Closer Charles", "Remnant Violet", "Briar Witch Iseria", "Hellion Lua", "Operator Sigret", "Pirate Captain Flan", "Sea Phantom Politis", "Archdemon's Shadow", "Eternal Wanderer Ludwig", "Harsetti", "Requiem Roana", "Specter Tenebria", "Top Model Luluca", "Zio", "Blood Moon Haste", "Death Dealer Ray", "Escanor", "Gojo Satoru", "Goku", "Taro Sakamoto"]
        
        if (num < 2.5):
            return random.choice(fiveStar)
        elif (num < 27.5):
            return random.choice(fourStar)
        else:
            return random.choice(threeStar)

    def custom_intro(self, name: str):
        """Get custom intro quote for character"""
        quotes = {
            "Gojo": "\"Daijoubu da. Ore wa Saikyou desu~\"", 
            "Goku": "\"I heard you're pretty strong. Fight me.\"",
            "Commander Pavel": "\"Must I meddle with these insignificant... flies?\"", 
            "Specter Tenebria": "\"I will step on you.\"",
            "Escanor": "\"I have no reason to feel hatred towards those beneath me. All I feel towards them is pity.\"",
            "Arbiter Vildred": "\"Can you hear THE APPROACHING RUIN?!\"",
            "Harsetti": "\"You were all just insignificant motes of filth until I graced you with my presence.\"",
            "Mediator Kawerik": "\"She is... my everything.\"",
            "Sea Phantom Politis": "\"We can dance from dawn till dusk, darling...\"",
            "New Moon Luna": "\"I am neither human nor dragon, yet I carry the burdens of both.\"",
            "Taro Sakamoto": "\"Starting now... I'm going all out.\"",
            "Dragon Bride Senya": "\"I'll stay by your side till death do we part.\"",
            "Briar Witch Iseria": "\"It hurts...\"",
            "Conqueror Lilias": "\"The march of Perland stops for no one!\"",
            "Fallen Cecilia": "\"My spear shall not stop till I eradicate the last of every Wind.\"",
            "Empyrean Ilynav": "\"Onward! We shall not give in to despair!\"",
            "Solitaria of the Snow": "\"Fwooo~oooosh! The Princess is here!\"",
            "Requiem Roana": "\"If you can promise me eternity, darling... I shall be yours for the rest of your life.\"",
            "Lone Crescent Bellona": "\"...Dipodoid.\"",
            "Hellion Lua": "\"you'll treat Lua well, won't you?\"",
            "Ruele of Light": "\"Looks like today is our Lucky day!\"",
            "Bystander Hwayoung": "\"I'm so sick of everything. I wish I could just... drift away with the wind.\"",
            "Top Model Luluca": "\"Pop, flash, boom! The idol of your dreams stands before you!\"",
            "Last Rider Krau": "\"Agent 007, reporting for Duty.\"",
            "Lionheart Cermia": "\"Well, this just got a lot more interesting! You're not half bad!\"",
            "Judge Kise": "\"I shall follow my duty till the end of the world.\"",
            "Astromancer Elena": "\"When I speak, you listen. When I move, you follow... Thus, you shall prove your usefulness.\"",
            "Straze": "\"Fate catches up with everyone. Not even gods can escape its wrath.\"",
            "Pirate Captain Flan": "\"Hop aboard, matey! I'll give you everything you desire...\"",
            "Zio": "\"You are mine. Servants. Slaves. Weapons. And you will obey…\"",
            "Death Dealer Ray": "\"Stay still. This won't hurt a bit...\"",
            "Navy Captain Landy": "\"Where the hell is that sly sea rat?! I'll get her! Hey, you!\"",
            "Blood Moon Haste": "\"My name is Haste Lenox. I don't usually speak with peasants, but perhaps I'll make an exception for you.\""
        }
        return quotes.get(name, "-1")

    @commands.command(name="mlpull", aliases=["ml", "mpull", "Ml", "ML"])
    async def mlpull_command(self, ctx):
        """Moonlight summoning simulator"""
        if ctx.channel.id in Config.MLPULL_ALLOWED_CHANNELS:
            name = ctx.author.display_name
            num = random.random() * 100
            if (num < 2.5):
                await ctx.reply("**A brilliant shower of Purple sparks blossom before you. This meeting was destined by the stars, you must be happy.**", mention_author=False)
            elif (num < 27.5):
                await ctx.reply("*There's a bright flash yet no spark. That's okay, the brightest stars need no spark to be seen.*", mention_author=False)
            else:
                await ctx.reply("Neither flash nor spark meets your eye, but perhaps the horizon brings greater fortune.", mention_author=False)
            result = self.sim_pull(num)
            time.sleep(1)
            cusint = self.custom_intro(result)
            if cusint != "-1":
                await ctx.send(f'***{cusint}***')
            time.sleep(1)
            await ctx.send(f"**{name}**, you have pulled... **{result}**.")
        else: 
            await ctx.send("Due to the amount of clutter this command creates, it is requested that you use it in the designated ciderbot channel. thank you.")

    @commands.command(name="echo")
    async def echo_command(self, ctx, *, input: str):
        """Admin only echo command"""
        if ctx.author.id != Config.ADMIN_USER_ID:
            await ctx.send("Who the hell are you?")
            return
        try: 
            await ctx.send(input)
            await ctx.message.delete()
        except Exception:
            await ctx.send("don't do that, please.")

async def setup(bot):
    await bot.add_cog(FunCommands(bot))
