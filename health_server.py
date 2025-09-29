from flask import Flask
import threading

class HealthServer:
    def __init__(self, bot):
        self.bot = bot
        self.app = Flask(__name__)
        self.setup_routes()
    
    def setup_routes(self):
        @self.app.route('/')
        def health_check():
            if self.bot.is_ready():
                return "Bot is up and running! ✅", 200
            else:
                return "Bot is down ❌", 503

        @self.app.route('/status')
        def bot_status():
            if self.bot.is_ready():
                guild_count = len(self.bot.guilds)
                latency = round(self.bot.latency * 1000) if self.bot.latency else 0
                return f"Bot Status: Online ✅\nConnected to {guild_count} servers\nLatency: {latency}ms", 200
            else:
                return "Bot Status: Offline ❌", 503
    
    def start(self):
        """Start the Flask server in a separate thread"""
        flask_thread = threading.Thread(target=self._run_server)
        flask_thread.daemon = True
        flask_thread.start()
        print("Health check server started on port 5000")
    
    def _run_server(self):
        self.app.run(host='0.0.0.0', port=5000, debug=False)