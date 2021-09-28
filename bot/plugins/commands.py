#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & @Mrk_YT

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption ="❤️ 𝚃𝚑𝚊𝚗𝚔𝚢𝚘𝚞 𝙵𝚘𝚛 𝚄𝚜𝚒𝚗𝚐 𝙾𝚞𝚛 𝚂𝚎𝚛𝚟𝚒𝚌𝚎 𝙿𝚕𝚎𝚊𝚜𝚎 𝚂𝚞𝚙𝚙𝚘𝚛𝚝 𝚄𝚜 𝙱𝚢 𝚂𝚑𝚊𝚛𝚒𝚗𝚐 𝙾𝚞𝚛 𝙲𝚑𝚊𝚗𝚗𝚎𝚕/𝙶𝚛𝚘𝚞𝚙 𝙻𝚒𝚗𝚔 𝚃𝚘 𝚈𝚘𝚞𝚛 𝙵𝚛𝚒𝚎𝚗𝚍𝚜 \n\n❁𝕁𝕠𝕚𝕟 𝕆𝕦𝕣 ℂ𝕙𝕒𝕟𝕟𝕖𝕝𝕤❁  \n\n⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱  \n\n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑: @mcnewmovies➻ \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑 : @MCmoviesall➻ \n👥𝕲𝖗𝖔𝖚𝖕 : @Movies_Club_2019 ➻ \n👥𝕲𝖗𝖔𝖚𝖕 : @Movies_Club_2019",
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝙎𝙃𝘼𝙍𝙀', url="https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/Movies_Club_2019")
                ],
                [
                    InlineKeyboardButton('𝙂𝙍𝙊𝙐𝙋', url="https://t.me/Movies_Club_2019"),
                    InlineKeyboardButton('𝙊𝙏𝙏 𝙍𝙀𝙇𝙀𝘼𝙎𝙀', url="https://t.me/mcnewmovies")
                ],
                [
                    InlineKeyboardButton('𝙎𝙐𝙋𝙋𝙊𝙍𝙏', url="https://t.me/joinchat/GRyjgnhqIdtmNjI9"),
                    InlineKeyboardButton('𝘾𝙃𝘼𝙉𝙉𝙀𝙇', url="https://t.me/mcallmovies")
                ]
            ]
        )
    )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝙎𝙃𝘼𝙍𝙀', url="https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/Movies_Club_2019")
                ],
                [
                    InlineKeyboardButton('𝙂𝙍𝙊𝙐𝙋', url="https://t.me/Movies_Club_2019"),
                    InlineKeyboardButton('𝙊𝙏𝙏 𝙍𝙀𝙇𝙀𝘼𝙎𝙀', url="https://t.me/mcnewmovies")
                ],
                [
                    InlineKeyboardButton('𝙎𝙐𝙋𝙋𝙊𝙍𝙏', url="https://t.me/joinchat/GRyjgnhqIdtmNjI9"),
                    InlineKeyboardButton('𝘾𝙃𝘼𝙉𝙉𝙀𝙇', url="https://t.me/mcallmovies")
                ]
            ]
        )
    )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝙎𝙃𝘼𝙍𝙀', url="https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/Movies_Club_2019")
                ],
                [
                    InlineKeyboardButton('𝙂𝙍𝙊𝙐𝙋', url="https://t.me/Movies_Club_2019"),
                    InlineKeyboardButton('𝙊𝙏𝙏 𝙍𝙀𝙇𝙀𝘼𝙎𝙀', url="https://t.me/mcnewmovies")
                ],
                [
                    InlineKeyboardButton('𝙎𝙐𝙋𝙋𝙊𝙍𝙏', url="https://t.me/joinchat/GRyjgnhqIdtmNjI9"),
                    InlineKeyboardButton('𝘾𝙃𝘼𝙉𝙉𝙀𝙇', url="https://t.me/mcallmovies")
                ]
            ]
        )
    )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('♻️ɢʀօʊք♻️', url='https://t.me/Movies_Club_2019'),
        InlineKeyboardButton('🛠️ɦɛʟք🛠️', callback_data="help")
    ],[
        InlineKeyboardButton('🎞️օȶȶ ʊքɖǟȶɛֆ🎞️', url='https://t.me/mcnewmovies')
   ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
                chat_id = update.chat.id,
                photo= "https://telegra.ph/file/fe98b3ef0ecd39f908a2f.jpg",
                caption=f"<b>😎ഞാൻ ധാ 👉 @Movies_Club_2019 👈ഇവിടുത്തെ കില്ലാടി ആണ്</b>\n <b><u>എന്റെ പവർ കാണാണോ ഗ്രൂപ്പിൽ കേറി വാ</u></b>",
    reply_markup=reply_markup,        reply_to_message_id=update.message_id
            )



@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('ℍ𝕆𝕄𝔼', callback_data='start'),
        InlineKeyboardButton('𝔸𝔹𝕆𝕌𝕋', callback_data='about')
    ],[
        InlineKeyboardButton('ℂ𝕃𝕆𝕊𝔼', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('𝐎𝐖𝐍𝐄𝐑', url='https://t.me/Myfreak123')
    ],[
        InlineKeyboardButton('𝐆𝐑𝐎𝐔𝐏', url='https://t.me/Movies_Club_2019')
    ],[
        InlineKeyboardButton('𝐇𝐎𝐌𝐄', callback_data='start'),
        InlineKeyboardButton('𝐂𝐋𝐎𝐒𝐄', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
