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
    
    HELP_TEXT = """How to Use me 🤔
    
1. <b>Send url</b>
        <i> if you need custom File Name do Like this ☛ (Link|New Name with Extension).</i>
2. <b>Send Custom Thumbnail </b>(Optional).
3. <b>Select the button.</b>
   » <b>SS+Video</b> - File as video with Screenshots
   » <b>SS+File</b>  - File with Screenshots
   » <b>Video</b>  - File as video without Screenshots
   » <b>File</b>  - File without Screenshots
   
  <b> Thats it, I will Do Rest of it 😌</b>
<b>check /about to Know about this bot</b>
"""
    
    ABOUT_TEXT = """Hi {},
  
<b>✪ » My Name : URLUploader bot
✪ » Creator : </b><a href="https://telegram.dog/oo7robot"> This Person </a>
✪ » <b>Credits : Everyone in this journey
✪ » Language : Python 3
✪ » Library : Pyrogram asyncio 
✪ » Cloned From : Spechide Source code
✪ » Source Code : </b> <a href="https://github.com"> click here </a>
✪ »<b> Server : Heroku
✪ » Build Status : v3 </b>
"""
    
    DONATE_TEXT = """**__Thanks for showing interest in donation.__**
 
All My Bots are hosted in free Server, if you Likes ma Works, & interested you donate some money it will be helpful for me to Pay my Internet Bills ☺️
**For Donate:** Message ** @OO7ROBot **"""
    
    
    
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
        
          

    
    
    
    

    
    
    
