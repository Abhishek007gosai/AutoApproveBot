from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from Script import text
from config import ADMIN

@Client.on_callback_query()
async def callback_query_handler(client, query: CallbackQuery):
    if query.data == "start":
        await query.message.edit_caption(
            caption=text.START.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ  ⇆', url=f"https://telegram.me/QuickAcceptBot?startgroup=true&admin=invite_users")],
                [InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
                 InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help')],
                [InlineKeyboardButton('⇆ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ⇆', url=f"https://telegram.me/QuickAcceptBot?startchannel=true&admin=invite_users")]
            ])
        )

    elif query.data == "help":
        await query.message.edit_caption(
            caption=text.HELP.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('ᴜᴘᴅᴀᴛᴇ', url='https://t.me/AnimeNexusNetwork/160'),
                 InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', url='https://t.me/EternalsHelplineBot')],
                [InlineKeyboardButton('ʙᴀᴄᴋ', callback_data="start"),
                 InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data="close")]
            ])
        )

    elif query.data == "about":
        await query.message.edit_caption(
            caption=text.ABOUT,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋', url='https://t.me/EternalsHelplineBot')],
                [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="start"),
                 InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]
            ])
        )

    elif query.data == "close":
        await query.message.delete()
