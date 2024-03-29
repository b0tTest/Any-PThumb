#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | MyTestBotZ

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import math
import os
import time

# the secret configuration specific things
#if bool(os.environ.get("WEBHOOK", False)):
from sample_config import Config
#else:
 #   from config import Config

# the Strings used for this "thing"
from translation import Translation


async def progress_for_pyrogram(
    current,
    total,
    ud_type,
    message,
    start
):
    now = time.time()
    diff = now - start
   # if round(diff % 10.00) == 0 or current == total:
    if round(diff % 3.00) > 2.999 or current == total:
        # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
       # speed = current / diff
        speed = current / diff * 10
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)
        time_to_completion = TimeFormatter(milliseconds=time_to_completion)

        progress =  "\n<b>Uploading......</b> \n{0}{1} {2}%\n".format(
            ''.join(["▰" for i in range(math.floor(percentage / 10))]),
            ''.join(["▱" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2))

        tmp = progress + "<b> 📥 Uploaded      : {0}\n 🐌 Speed...........: {2}/s\n ⏱ Time Left...... : {4}\n\n┈┈••✿ @MyTestBotZ ✿••┈┈\nTotal size  : {1} \nE.T.A......... : {3}</b>\n\nThanks for Using @AnyUrlDLbot".format(
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            # elapsed_time if elapsed_time != '' else "0 s",
            estimated_total_time if estimated_total_time != '' else "0 s",
            time_to_completion if time_to_completion != '' else  "0 s"
        )
        try:
            await message.edit(
                text="{}\n {}".format(
                    ud_type,
                    tmp
                )
            )
        except:
            pass


def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]
