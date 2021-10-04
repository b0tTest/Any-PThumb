class Translation(object):
    START_TEXT = """<b>Hai {} </b>,
a simple Telegram URL Upload Bot!
it can <b>UPLOAD almost all Direct Links to Telegram as File/Video</b>
 
🚨 Dont Upload PORN video🔞 Links you will Get PERMANENT BAN 🚨


┈┈┈••💙✿❤✿💚••┈┈┈
"""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "you are that much Rich????"
    FORMAT_SELECTION = """<b>Select the desired format</b> 

🎞  - Stream format (left side)
📁  - File format (right side)

If you want to set custom thumbnail, send photo 
or Use auto-generated <a href='{}'>📸</a> <b>Thumbnail.</b>"""
    SET_CUSTOM_USERNAME_PASSWORD = """ """
    NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_START = """<b>Downloading to my server 📥</b>
   
  <code>Please wait...⏳ 🙇🙇🙇
  it takes time depend on File Size</code>
  
  <b>Note : if its Take too LonG ....set an Custom Thumbnail & Try Again</b>"""
    UPLOAD_START = """<b>Yay,File Download Successfully 😊</b>
    <code>Now Uploading to Telegram 📤</code>
    
 """
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = """**Thank you for Using Me.** 
    **Now you can send another Link** 
    @myTestbotz"""
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " @AnyUrlDLbot"
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """Current plan details
-------- 
<b>User Name : {} </b>
<b>Telegram ID :</b> <code>{}</code>
<b>Plan name :</b> Free User
<b>Expires on :</b> 31/12/2021"""
    HELP_USER = """How to Use me 🤔
    
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
    About = """Hi {},
  
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

    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /rename with custom thumbnail support"
    AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days."
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/FFMpegRoBot"
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """<b>Cannot Process.</b>
    
 <b>To Prevent Spamming & Floodwait ➠ Only 1 request per {} minutes.</b>

<i>Please Try {} seconds later.</i>"""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    AUTH_CHANNEL_TEXT = "You must Join Updates Channel to use me."
    DOWNLOADING = "**AnaliZing ⏳...**"
    YOUTUBE_LINK = """<b>♨️Downloading from youtube Link, use our</b> <a href="https://t.me/MyTestBotZ/260">Youtube Bots</a>"""
    AUTH_CHANNEL_TEXT = """**You must Join Updates Channel to use me😌.**
    
    <i>Due to Overload, Only Channel Subscribers can use this Bot!🤷</i>
    """
    
    
    CHECKING_LINK = "<code>Analysing Your Link</code>⏳"
    BANNED_USER_TEXT = "<code>You are Banned!</code>"
    REPORT_SITE_TEXT = "<code>Sorry not uploading in this site here because this site is reporting site.</code>"
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    FORCE_SUBSCRIBE_TEXT = """**You must Join Updates Channel to use me😌.**
    
    <i>Due to Overload, Only Channel Subscribers can use this Bot!🤷</i>
    """
    
    SHOW_THUMB = "<b>Your Permanent Thumbnail ⤴️ \nUse /delthumb to clear this thumbnail</b>."
    NO_THUMB = "<b>No saved thumbnails Found!!\n\nSend an image to save it as your thumbnail permanently.</b>"
    

