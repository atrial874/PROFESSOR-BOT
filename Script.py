class script(object):   
    HELP_TXT = """π·π΄π {}
π·π΄ππ΄ πΈπ ππ·π΄ π·π΄π»πΏ π΅πΎπ πΌπ π²πΎπΌπΌπ°π½π³π."""

    ABOUT_TXT = """β― πΌπ π½π°πΌπ΄ : {}
β― π²ππ΄π°ππΎπ : <a href=https://t.me/c4christy>CHRISTY</a>
β― BOT SERVER : AML DOMAIN
β― BOT VERSION: DAILY ON A NEW π"""

    SOURCE_TXT = """ ΰ΄ΰ΅ΰ΄ΰ΅ΰ΄ΰ΅ ΰ΄ΰ΄³ΰ΅ΰ΄³ΰ΅»π """
    FILE_TXT = """MADE FOR ADMINS BROπ"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and α©αα©α­  will respond whenever a keyword is found the message

<b>NOTE:</b>
1. This bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>

β’ <code>/g_filter off</code> use this commoand + on/off in your group to control global filter in your group"""
   
    BUTTON_TXT = """Help: <b>Buttons</b>

-this bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:xxxxxxxxxxxx)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """**Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db.**"""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of this bot

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specifed user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""

    ADMIN_TXT = """<b>Ι΄α΄α΄α΄:</b>
<code>TΚΙͺs Mα΄α΄α΄Κα΄ OΙ΄ΚΚ Wα΄Κα΄s Fα΄Κ MΚ Aα΄α΄ΙͺΙ΄s</code>"""

    US_CHAT_TXT = """<b>Ι΄α΄α΄α΄:</b>
<code>TΚΙͺs Mα΄α΄α΄Κα΄ OΙ΄ΚΚ Wα΄Κα΄s Fα΄Κ MΚ Aα΄α΄ΙͺΙ΄s</code>"""

    G_FIL_TXT = """<b>Ι΄α΄α΄α΄:</b>
<code>TΚΙͺs Mα΄α΄α΄Κα΄ OΙ΄ΚΚ Wα΄Κα΄s Fα΄Κ MΚ Aα΄α΄ΙͺΙ΄s</code>"""

    STATUS_TXT = """<b> TOTAL FILES: <code>{}</code></b>
<b>TOTAL USERS: <code>{}</code></b>
<b>TOTAL CHATS: <code>{}</code></b>
<b>αβΊ USED STORAGE: <code>{}</code> πΌπ±</b>
<b>αβΊ FREE STORAGE: <code>{}</code> πΌπ±</b>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
   
    ZOMBIES_TXT = """NOT A ZOMBIEπ"""

    IMAGE_TXT = """NOT MADE FOR EDITING BRUH"""

    RESTRIC_TXT = """β€ πππ₯π©: Mα΄α΄α΄ π«

πππππ πππ πππ ππππππππ π πππππ πππππ πππ πππ ππ ππππππ πππππ πππππ ππππ πππππππππππ’.

βͺ/ban: π³π π»πΊπ πΊ πππΎπ πΏπππ πππΎ πππππ.
βͺ/unban: π³π πππ»πΊπ πΊ πππΎπ ππ πππΎ πππππ.
βͺ/tban: π³π ππΎπππππΊππππ π»πΊπ πΊ πππΎπ.
βͺ/mute: π³π ππππΎ πΊ πππΎπ ππ πππΎ πππππ.
βͺ/unmute: π³π ππππππΎ πΊ πππΎπ ππ πππΎ πππππ.
βͺ/tmute: π³π ππΎπππππΊππππ ππππΎ πΊ πππΎπ.

β€ π­πππΎ:
πΆππππΎ πππππ /tmute ππ /tban πππ ππππππ½ πππΎπΌππΏπ πππΎ ππππΎ πππππ.

βπ€ππΊππππΎ: /ππ»πΊπ 2π½ ππ /πππππΎ 2π½.
πΈππ πΌπΊπ πππΎ ππΊπππΎπ: π/π/π½. 
 β’ π = ππππππΎπ
 β’ π = πππππ
 β’ π½ = π½πΊππ"""


    PIN_TXT ="""<b>PIN MODULE</b>
<b>πΏπΈπ½ π° πΌπ΄πππ°πΆπ΄../</b>

<b>π°π»π» ππ·π΄ πΏπΈπ½ ππ΄πΏπ»π°ππ΄π³ π²πΎπΌπΌπ°π½π³π π²π°π½ π±π΄ π΅πΎππ½π³ π·π΄ππ΄::</b>

<b>ππ²πΎπΌπΌπ°π½π³π π°π½π³ πππ°πΆπ΄π</b>

β /pin :- ππΎ πΏπΈπ½ ππ·π΄ πΌπ΄πππ°πΆπ΄ πΎπ½ ππΎππ π²π·π°ππ
β /unpin :- ππΎ ππ½πΏπΈπ½ ππ·π΄ π²ππππ΄π΄π½π πΏπΈπ½π½π΄π³ πΌπ΄ππ°π°πΆπ΄"""

    PASTE_TXT = """."""

    TTS_TXT = """
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ IMDb can translate texts to 200+ languages."""

    PINGS_TXT =""" . """

    TELE_TXT = """."""

    JSON_TXT ="""."""

    PURGE_TXT = """<b>Purge</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

β /purge :- Delete All Messages From The Replied To Message, To The Current Message"""

    CREATOR_REQUIRED = """β<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "β **Arguments Required**"
      
    KICKED = """βοΈ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """π? Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """β<b>ΰ΄ΰ΄¨ΰ΅ΰ΄¨ΰ΅ Admin ΰ΄ΰ΄ΰ΅ΰ΄ΰ΄€ΰ΅ΰ΄€ ΰ΄Έΰ΅ΰ΄₯ΰ΄²ΰ΄€ΰ΅ΰ΄€ΰ΅ ΰ΄ΰ΄Ύΰ΅» ΰ΄¨ΰ΄Ώΰ΄ΰ΅ΰ΄ΰ΄Ώΰ΄²ΰ΅ΰ΄² ΰ΄ͺΰ΅ΰ΄ΰ΅ΰ΄΅ΰ΄Ύ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """βοΈ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>ΰ΄ΰ΄ͺΰ΅ΰ΄ͺΰ΅ ΰ΄ΰ΄²ΰ΅ΰ΄²ΰ΄Ύΰ΄ ΰ΄ΰ΄ΰ΄Ώΰ΄ΰ΅ΰ΄ΰ΅ΰ΄?ΰ΄Ύΰ΄±ΰ΅ΰ΄±ΰ΄Ώ ΰ΄€ΰ΄°ΰ΄Ύΰ΄...</b>"""
      
    CARB_TXT = """βΎοΈππππ£ ππ’π₯ πππ₯ππ’π‘β½οΈ
π²π°ππ±πΎπ½ πΈπ π° π΅π΄πππππ΄ ππΎ πΌπ°πΊπ΄ ππ·π΄ πΈπΌπ°πΆπ΄ π°π ππ·πΎππ½ πΈπ½ ππ·π΄ ππΎπΏ ππΈππ· ππΎπππ΄ ππ΄πππ.
π΅πΎπ πππΈπ½πΆ ππ·π΄ πΌπΎπ³ππ»π΄ πΉπππ ππ΄π½π³ ππ·π΄ ππ΄ππ π°π½π³ ππ΄πΏπ»π ππΎ πΈπ ππΈππ· /carbon π²πΎπΌπΌπ°π½π³ ππ·π΄ π±πΎπ ππΈπ»π» ππ΄πΏπ»π ππΈππ· ππ·π΄ π²π°ππ±πΎπ½ πΈπΌπ°πΆπ΄"""

    FOND_TXT = """βΎοΈππππ£ ππ’π₯ ππ’π‘π§π¦β½οΈ
π΅πΎπ½π πΈπ π° πΌπΎπ³ππ»π΄ π΅πΎπ πΌπ°πΊπ΄ ππΎππ ππ΄ππ ππππ»πΈππ·.
π΅πΎπ πππ΄ ππ·π°π π΅π΄πππππ΄ πππΏπ΄ /font <your text> ππ·π΄π½ ππΎππ ππ΄ππ πΈπ ππ΄π°π³π."""

    SHARE_TXT = """βΎοΈππππ£ ππ’π₯ π¦πππ₯π π§ππ«π§β½οΈ

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:
β’ /share - πππππ’ ππππ π°ππ’ πππ‘π ππ ππππ ππππ π²ππππππ """




    


    

