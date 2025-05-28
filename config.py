import os
import time

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7693803634:AAFIWfW8gfzMYv-G5-I9hAnge1mYFVkspio")

    # Get from my.telegram.org (or @UseTGXBot)
    API_ID = int(os.environ.get("API_ID", 12618934))

    # Get from my.telegram.org (or @UseTGXBot)
    API_HASH = os.environ.get("API_HASH", "49aacd0bc2f8924add29fb02e20c8a16")
    
    # Database URL from https://cloud.mongodb.com/
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://batman13:batman13@batman.sawvl.mongodb.net/?retryWrites=true&w=majority&appName=batman")

    # Your database name from mongoDB
    DATABASE_NAME = str(os.environ.get("DATABASE_NAME", "batman"))

    # ID of users that can use the bot commands
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5032034594").split())

    # To save user details (Useful for getting userinfo and total user counts)
    # May reduce filter capacity :(
    # Give yes or no
    SAVE_USER = os.environ.get("SAVE_USER", "no").lower()

    # To record start time of bot
    BOT_START_TIME = time.time()

    # OPTIONAL - To set alternate BOT COMMANDS
    ADD_FILTER_CMD = os.environ.get("ADD_FILTER_CMD", "add")
    DELETE_FILTER_CMD = os.environ.get("DELETE_FILTER_CMD", "del")
    DELETE_ALL_CMD = os.environ.get("DELETE_ALL_CMD", "delall")
    CONNECT_COMMAND = os.environ.get("CONNECT_COMMAND", "connect")
    DISCONNECT_COMMAND = os.environ.get("DISCONNECT_COMMAND", "disconnect")

    # Go to https://dashboard.heroku.com/account, scroll down and press Reveal API
    # To check dyno status
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")


    # To record start time of bot
    BOT_START_TIME = time.time()
