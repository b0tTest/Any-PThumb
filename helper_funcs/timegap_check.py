#MytestBotz

import time
from sample_config import Config
from helper_funcs.display_progress import TimeFormatter

async def timegap_check(update):
    """Checking the time gap is completed or not 
    and checking the parallel process"""

    if update.from_user.id in Config.TIME_GAP_STORE:
        if int(time.time() - Config.TIME_GAP_STORE[update.from_user.id]) < Config.TIME_GAP:
            minute = round(Config.TIME_GAP/60)
            text = f"""<b>Cannot Pocess,</b>\n\n➠ <b>{minute} Minute</b> <i>Flood Control is Active so Please Wait</i><b> {TimeFormatter((int(Config.TIME_GAP_STORE[update.from_user.id]) + Config.TIME_GAP - int(time.time())) * 1000)} </b><i>Before Next Request</i>"""
            await update.reply_text(
                text=text,
                parse_mode="html",
                quote=True
            )
            return True
        else:
            del Config.TIME_GAP_STORE[update.from_user.id]
            return False
    else:
        return False
