#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | MyTestBotZ

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
from blocked import Blocked
  
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)
 
##Hotstar
@pyrogram.Client.on_message(pyrogram.Filters.regex(pattern=".*hotstar.com/*"))
async def porn_hotstar(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Blocked.ABUSE_HOTSTAR,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )

    
#Mega Link
@pyrogram.Client.on_message(pyrogram.Filters.regex(pattern=".*mega.nz/*"))
async def porn_mega(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Blocked.ABUSE_MEGA,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
    
#xvideo 
@pyrogram.Client.on_message(pyrogram.Filters.regex(pattern=".*http://www.xvideos.com/*|.*xvideos.com/*"))
async def porn_xvideos(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Blocked.ABUSE_XVIDEOS,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
    
#xnxx
@pyrogram.Client.on_message(pyrogram.Filters.regex(pattern=".*http://www.xnxx.com/*|.*xnxx.com/*"))
async def porn_xnxx(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Blocked.ABUSE_XNXX,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )

#pornhub
@pyrogram.Client.on_message(pyrogram.Filters.regex(pattern=".*http://www.pornhub.com/*|.*pornhub.com/*"))
async def porn_pornhub(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Blocked.ABUSE_PORNHUB,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
    
#xHamster
@pyrogram.Client.on_message(pyrogram.Filters.regex(pattern=".*http://www.xhamster.com/*|.*xhamster.com/*"))
async def porn_xhamster(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Blocked.ABUSE_XHAMSTER,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )

