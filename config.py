import os

class Config:
    """Configuration class for Discord bot"""
    
    # Bot settings
    COMMAND_PREFIX = '?'
    
    # Discord token from environment
    DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    
    # Guild settings
    TEST_GUILD_ID = 1323170377395863722
    
    # Channel restrictions
    MLPULL_ALLOWED_CHANNELS = [1328505904160837673, 1328897923374907403]
    
    # Admin user ID for restricted commands
    ADMIN_USER_ID = 319296643667066890
    
    # Health check server settings
    HEALTH_CHECK_PORT = 5000
    HEALTH_CHECK_HOST = '0.0.0.0'
    
    @classmethod
    def validate(cls):
        """Validate that required configuration is present"""
        if not cls.DISCORD_BOT_TOKEN:
            raise ValueError("DISCORD_BOT_TOKEN not found in environment variables")
        return True