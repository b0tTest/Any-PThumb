import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
from PIL import Image	
import time	
import numpy

from translation import Translation
from helper_funcs.database import *


@pyrogram.Client.on_message(pyrogram.Filters.photo)
async def save_photo(bot, update):
    
    if update.media_group_id is not None:
        download_location = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + "/" + str(update.media_group_id) + "/"
        if not os.path.isdir(download_location):
            os.makedirs(download_location)
        await df_thumb(update.from_user.id, update.message_id)
        await bot.download_media(
            message=update,
            file_name=download_location
        )
    else:
        download_location = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
        await df_thumb(update.from_user.id, update.message_id)
        await bot.download_media(
            message=update,
            file_name=download_location
        )
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.SAVED_CUSTOM_THUMB_NAIL,
            reply_to_message_id=update.message_id
        )


@pyrogram.Client.on_message(pyrogram.Filters.command(["delthumb"]))
async def delete_thumbnail(bot, update):
    
    thumb_image_path = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
    
    try:
        await del_thumb(update.from_user.id)
    except:
        pass

    try:
        os.remove(thumb_image_path)
    except:
        pass

    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.DEL_ETED_CUSTOM_THUMB_NAIL,
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["showthumb"]))
async def show_thumb(bot, update):
    

    thumb_image_path = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
    if not os.path.exists(thumb_image_path):
        mes = await thumb(update.from_user.id)
        if mes != None:
            m = await bot.get_messages(update.chat.id, mes.msg_id)
            await m.download(file_name=thumb_image_path)
            thumb_image_path = thumb_image_path
        else:
            thumb_image_path = None    
    
    if thumb_image_path is not None:
        try:
            await bot.send_photo(
                chat_id=update.chat.id,
                photo=thumb_image_path,
                caption=Translation.SHOW_THUMB
            )
        except:
            pass
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.NO_THUMB,
            reply_to_message_id=update.message_id
        )
