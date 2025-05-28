import os
import pyrogram
from config import Config

# Flask-related imports
from threading import Thread
from flask import Flask

# Start Flask dummy app for Koyeb health check
app_web = Flask(__name__)

@app_web.route('/')
def home():
    return "Bot is alive!"

def run_web():
    port = int(os.environ.get("PORT", 8000))
    app_web.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Start the dummy web server in a new thread
    Thread(target=run_web).start()

    # Set up Pyrogram bot
    plugins = dict(root="plugins")
    app = pyrogram.Client(
        "filter bot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300
    )
    Config.AUTH_USERS.add(str(680815375))
    app.run()
