import discord
from discord.ext import commands
import asyncio
import os
from config import Config
from dotenv import load_dotenv

load_dotenv('.env')

class DiscordBot(commands.Bot):
    """Main Discord bot class"""
    
    def __init__(self):
        # Set up intents
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        
        super().__init__(
            command_prefix=Config.COMMAND_PREFIX,
            intents=intents
        )
    
    async def setup_hook(self):
        """Load all cogs when bot starts up"""
        cogs_to_load = [
            'cogs.utilities',
            'cogs.fun_commands', 
            'cogs.moderation',
            'cogs.skill_check',
            'cogs.cm_info',
            'cogs.announcements',
            'cogs.war_thunder'
        ]
        
        for cog in cogs_to_load:
            try:
                await self.load_extension(cog)
                print(f'✅ Loaded {cog}')
            except Exception as e:
                print(f'❌ Failed to load {cog}: {e}')
        
        # Sync commands to test guild and globally
        try:
            test_guild = discord.Object(id=Config.TEST_GUILD_ID)
            self.tree.copy_global_to(guild=test_guild)
            await self.tree.sync(guild=test_guild)
            print(f"Commands synced to test guild")
            
            synced = await self.tree.sync()
            print(f"Synced {len(synced)} global commands")
        except Exception as e:
            print(f"Error syncing commands: {e}")

async def main():
    """Main entry point"""
    # Validate configuration
    try:
        Config.validate()
    except ValueError as e:
        print(f"Configuration error: {e}")
        return
    
    # Create and run bot
    bot = DiscordBot()
    
    try:
        await bot.start(os.getenv('DISCORD_BOT_TOKEN'))
    except KeyboardInterrupt:
        print("Bot shutting down...")
    except Exception as e:
        print(f"Bot error: {e}")
    finally:
        await bot.close()

if __name__ == '__main__':
    asyncio.run(main())