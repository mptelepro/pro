#sanmanasullavar errors fix akki tharanam š

import pyrogram
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import User, Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from info import API_ID
from info import API_HASH
from info import BOT_TOKEN
from OMDB import get_movie_info
#=======================================================================

START_MSG = f"š§šŗš, \nšØ'š šŗ š²ššššš¾ š³š¾šš¾šššŗš š”šš š³š š¦š¾š š¬šššš¾ šØššæš š“šššš š®š¬š£š»\n \nš²š¾šš½ š¬š¾ š³šš¾ š¬šššš¾ š­šŗšš¾ š³š š¦š¾š šØššæš š š»ššš šØš"

STICKER = 'CAACAgUAAxkDAALjS2F9dI-C4OaXKkSgsAxjX1mkofkKAAJXBAAC6aXoV2X6ud6KqXzUHgQ'  

#=======================================================================

Sam = Client(
    session_name="OMDb-Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

print("Starting Bot..")

#=======================================================================

@Sam.on_message(filters.command(['start']) & filters.private)
def start(client, cmd):
         cmd.reply_sticker(STICKER)
         cmd.reply_text(START_MSG)
               
@Sam.on_message(filters.text)
async def imdbcmd(client, message):
    movie_name = message.text
    movie_info = get_movie_info(movie_name)
    if movie_info:
                  poster = movie_info["pimage"]
                  urlid = movie_info['imdb_id']
                  buttons=[[InlineKeyboardButton('š šØš¬š£š»', url=f"https://www.imdb.com/title/{urlid}")]] 
                                                     
                  text=f"""š š³šššš¾ : <b>{movie_info['title']}</b>
                            
ā±ļø š±šššššš¾ : <b>{movie_info['duration']}</b>
š š±šŗšššš : <b>{movie_info['imdb_rating']}/10</b>
š³ļø šµššš¾š : <b>{movie_info['votes']}</b>

š š±š¾šš¾šŗšš¾ : <b>{movie_info['release']}</b>
š­ š¦š¾ššš¾ : <b>{movie_info['genre']}</b>
š š«šŗššššŗšš¾ : <b>{movie_info['language']}</b>
š š¢šššššš : <b>{movie_info['country']}</b>

š„ š£ššš¾š¼šššš : <b>{movie_info['director']}</b>
š š¶šššš¾šš : <b>{movie_info['writer']}</b>
š š²ššŗšš : <b>{movie_info['actors']}</b>

š šÆššš : <code>{movie_info['plot']}</code>"""
                  
                  if poster.startswith("https"):
                                                m = await message.reply_text("š„ššš½ššš š£š¾ššŗššš..")
                                                await message.reply_photo(photo=poster.replace("_SX300","_"), caption=text, reply_markup=InlineKeyboardMarkup(buttons))
                                                await m.delete()
                  else:
                       m = await message.reply_text("š²šššš,\nšØ š¢šŗš'š š„ššš½ šÆšššš¾šš.\nš²š¾šš½ššš š ššŗšššŗš»šš¾ š£š¾ššŗššš..")
                       await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
                       await sleep(4)
                       await m.delete()
    else:
        omdbbuttons=[[InlineKeyboardButton('š š²š¾šŗšš¼š š®š š¦ššššš¾.', url=f'https://google.com/search?q={movie_name.replace(" ","+")}')]]
        await message.reply_text(text="š¢šššš½š'š š„š¾šš¼š š£š¾ššŗššš\nš³šš š³š š¢šš¾š¼š šøššš š²šš¾ššššš.", reply_markup=InlineKeyboardMarkup(omdbbuttons))       


#=======================================================================
print("Bot Started!")
#=======================================================================

Sam.run()

#=======================================================================
