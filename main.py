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
        await self.load_all_cogs()
        
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
    
    async def load_all_cogs(self):
        """Load cogs from specific folders"""
        cog_folders = [
            'cogs.functional_programs', 
            'cogs.utilities'
        ]
        
        for folder in cog_folders:
            cog_path = folder.replace('.', '/')
            if os.path.exists(cog_path):
                for file in os.listdir(cog_path):
                    if file.endswith('.py') and not file.startswith('__'):
                        module_path = f"{folder}.{file[:-3]}"
                        try:
                            await self.load_extension(module_path)
                            print(f'✅ Loaded {module_path}')
                        except Exception as e:
                            print(f'❌ Failed to load {module_path}: {e}')

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