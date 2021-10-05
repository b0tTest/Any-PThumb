import pyrogram
from pyrogram import (
    Client,
    Filters,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

class Text(object):
    START_TEXT = """<b>Hai {} </b>,
a simple Telegram URL Upload Bot!
it can <b>UPLOAD almost all Direct Links to Telegram as File/Video</b>
 
🚨 Dont Upload PORN video🔞 Links you will Get PERMANENT BAN 🚨
┈┈┈••💙✿❤✿💚••┈┈┈
"""
    
    HELP_TEXT = """<b>How to Use me 🤔</b>
    
1. <b>Send any url</b>
        <i> if you need custom File Name do Like this ☛ (Link|New Name with Extension).</i>

2. <b>Send Custom Thumbnail </b>(Optional but Recommended).

3. <b>Select the button.</b>
   » <b>SS+Video</b> - File as video with Screenshots
   » <b>SS+File</b>  - File with Screenshots
   » <b>Video</b>  - File as video without Screenshots
   » <b>File</b>  - File without Screenshots
   
  <b> Thats it, I will Do Rest of it 😌</b>

➠ <a href="https://telegram.me/myTestbotz/73"> How to Download Gdrive files </a>
➠ <a href="https://telegram.me/myTestbotz/349"> How to Download Gdrive files </a>
➠

➠ <a href="https://telegram.me/MyTestBotZ/349"> Temporary Fix Thumbnail issues </a>
"""
    
    ABOUT_TEXT = """Hi {},
  
<b>✪ » My Name : URLUploader bot
✪ » Creator : </b><a href="https://telegram.dog/oo7robot"> This Person </a>
✪ »<b> Channel : <a href="https://telegram.dog/MyTestBotZ"> @MyTestBotZ </a>
✪ » Other Bots : <a href="https://telegram.dog/mybotzlist"> @MyBotZList </a>
✪ » Credits : Everyone in this journey
✪ » Language : Python 3
✪ » Library : Pyrogram asyncio 
✪ » Cloned From : Spechide Source code
✪ » Source Code : </b> <a href="https://github.com"> click here </a>
✪ »<b> Server : Heroku
✪ » Build Status : v3 </b>

"""
    
    DONATE_TEXT = """<b>Thanks for showing interest in donation.</b>
 
All My Bots are hosted in free Server, if you Likes ma Works, & interested you donate some money it will be helpful for me to Pay my Internet Bills ☺️
<b>For Donate:</b> Message <b> @OO7ROBot </b>"""
    
    THUMBNAIL_TEXT = """<b>Here Are The Available Commands In Custom Thumbnail </b>
    
⦿ <i> Send A Photo To Set The Custom Thumbnail (its Permanent) </i>

⦿ /showthumb : <i> For Checking The Current Thumbnail </i>
        
⦿ /delthumb : <i> For Deleting The Current Saved Thumbnail </i>
    
 
    """
    
    COMMAND_TEXT = """<b>Available Commands</b>

⍟ /start - <i>Checking Bot Online</i>

⍟ /help - <i>For more help</i>

⍟ /about - <i>For more about me</i>

⍟ /donate - <i>Donations</i>

⍟ /plan - <i>Plan details & user info</i>

⍟ /showthumb - <i>To view current thumbnail</i>

⍟ /delthumb - <i>To deleting current thumbnail</i>

    """
    
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📡Channel', url='https://telegram.me/MyTestBotZ'),
       # InlineKeyboardButton('Creator', url='https://telegram.me/OO7ROBOT')
        #],[
        InlineKeyboardButton('🖥Botslist', url='https://t.me/myTestbotz/15'),
        InlineKeyboardButton('👤 Creator', url='https://telegram.me/OO7ROBOT')
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
        InlineKeyboardButton('🖼️Custom Thumb', callback_data='cthumb'),
        InlineKeyboardButton('❣️All Commands', callback_data='cmd')
        ],[
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
    HBACK_BUTTONS = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🔙 Back', callback_data = 'help'),
                    InlineKeyboardButton('⛔ Close', callback_data = 'close')
                ]
            ]
        )
        
          

    
    
    
    

    
    
    
