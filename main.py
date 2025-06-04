import os
from bot import bot

if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))
