#  importing the main libraries

# importing pyrogram to connect telegram
from pyrogram import Client,filters

# importing os to process command in powershell
import os

# Telegram API_ID & API_HASH & BOT_TOKEN
API_ID = 123456 # Get this from my.telegram.org
API_HASH = "this is the hash key" # Get this from my.telegram.org
BOT_TOKEN = "this is the bot token" # Get This from Bot father

app = Client(api_id=API_ID,api_hash=API_HASH,bot_token=BOT_TOKEN)

@app.on_message(filters.command(["start"]))
def start(client,message):
    print(message)

@app.on_message(filters.command(["help"]))
def help(client,message):
    app.send_message(chat_id=message['from_user']['id'],text='<a href="">Get help from github</a>')
app.run()