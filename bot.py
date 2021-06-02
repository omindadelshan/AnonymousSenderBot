#    Copyright (C) 2021 - Infinity Bots
#    This programme is a part of JEAnonymousBot
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


import logging
from telethon import TelegramClient, events, Button
from decouple import config

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

bottoken = None
# start the bot
print("Starting...")
apiid = 6
apihash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
try:
    bottoken = config("BOT_TOKEN")
except:
    print("Environment vars are missing!")
    print("Bot is quiting...")
    exit()

if bottoken != None:
    try:
        JEBotZ = TelegramClient("bot", apiid, apihash).start(bot_token=bottoken)
    except Exception as e:
        print(f"ERROR!\n{str(e)}")
        print("Bot is quiting...")
        exit()
else:
    print("Environment vars are missing! Kindly recheck.")
    print("Bot is quiting...")
    exit()
    
    
@JEBotZ.on(events.NewMessage(pattern="^/start"))
async def start(event):
    await event.reply("Heya, I'm **Advanced Anonymous Sender** Bot.\nClick on help to find out how to use me.\n\n**@JEBotZ**", 
                       buttons=[[Button.inline("Help", data="help")], 
                                [Button.url("Channel", url="https://t.me/Infinity_Bots"), Button.url("Source", url="https://github.com/ImJanindu/AnonymousSenderBot")]])
    
 
@JEBotZ.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):
     await event.edit("**Help**\n\nUsing me you can anonymize the sender and add or change caption of a media file\n\n**Available Commands:**\n\n- /send (reply to media): Anonymize the sender.\n- /edit (caption) (reply to media): Add or change the caption and anonymize the sender.\n\n**@JEBotZ**", 
                        buttons=[[Button.inline("Back", data="start")]])
    
@JEBotZ.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
     await event.edit("Heya, I'm **Advanced Anonymous Sender** Bot.\nClick on help to find out how to use me.\n\n**@JEBotZ**", 
                       buttons=[[Button.inline("Help", data="help")], 
                                [Button.url("Channel", url="https://t.me/Infinity_Bots"), Button.url("Source", url="https://github.com/ImJanindu/AnonymousSenderBot")]])
    
    
@JEBotZ.on(events.NewMessage(pattern="^/send"))
async def anonymize(event):
     sed = await event.get_reply_message()
     await JEBotZ.send_file(event.chat.id, sed)
      
      
@JEBotZ.on(events.NewMessage(pattern="^/edit ?(.*)"))
async def caption(event):
     lel = await event.get_reply_message()
     cap = event.pattern_match.group(1)
     await JEBotZ.send_file(event.chat.id, lel, caption=cap) 
    
    
    
print("Bot has started!")
print("Do visit @JEBotZ.")
JEBotZ.run_until_disconnected()
  
