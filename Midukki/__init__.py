from aiohttp import web
from os import environ
from re import compile
from time import time
from .scripts import START_TXT, FILE_CAPTION_TXT, SPELLCHECK_TXT, IMDB_TEMPLATE_TXT, WELCOME_TXT

routes = web.RouteTableDef()
find = compile(r'^.\d+$')

def who_is_creator(id1, id2):
  # print(pass)
  text = (
   f"\nBot Created By {id2.first_name}" + "\n"
   f"\nBot Deployed By {id1.first_name}"
  )
  return text
    
class Accounts(object):
    API_ID = int(environ.get("API_ID", 27639102))
    API_HASH = environ.get("API_HASH","35142c1407be6264e68fb6bec5dcabd9")
    BOT_TOKEN = environ.get("BOT_TOKEN","5831408471:AAGASWCr4oMCSeZ_yudwiOLuSi7ghn_P-m8")
    BOT_PLUGINS = environ.get("BOT_PLUGINS", "Movie Search Bot")
    BOT_SESSIONS = environ.get("BOT_SESSION", "Movie Search Bot")

class Bots(object):
    BOT_ID = int(environ.get("BOT_ID", Accounts.BOT_TOKEN.split(":")[0]))
    BOT_NAME = None # "Movie Search Bot"
    BOT_MENTION = None # "@VJ_Movie_Search_RoBot"
    BOT_USERNAME = None # "VJ_Movie_Search_RoBot"
    #bot up time
    BOT_START_TIME = time()

class Customize(object):
    FILE_CAPTION = environ.get("FILE_CAPTION", FILE_CAPTION_TXT)
    SPELLCHECK_CAPTION = environ.get("SPELLCHECK_CAPTION", SPELLCHECK_TXT)
    IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", IMDB_TEMPLATE_TXT)
    WELCOME_CAPTION = environ.get("WELCOME_CAPTION", WELCOME_TXT)
    AUTO_DEL_TIME = int(environ.get("AUTO_DEL_TIME", "900"))

class Configs(object):
    # admins id
    ADMINS_ID = [int(admin) if find.search(admin) else admin for admin in environ.get('ADMINS_ID', '5606411877').split()]

    # bot information   
    COMMAND_PREFIXES = environ.get("COMMAND_PREFIXES", "/")
    if environ.get("BOT_PICS"):
        START_PICS = (environ.get("BOT_PICS", "https://telegra.ph/file/5ad2c57ae74bafb6efec1.jpg")).split()
    START_MESSAGE = environ.get("START_MESSAGE", START_TXT)

    # MongoDB information
    DATABASE_NAME = environ.get("DATABASE_NAME", "Advanced-Autofilter-Bot")
    DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://Demo123:Demo123@cluster0.qans7w0.mongodb.net/?retryWrites=true&w=majority")
    COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

    # Groups & Channels
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001844758544))
    SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/VJ_Bot_Disscussion')
    CHANNELS = [int(ch) if find.search(ch) else ch for ch in environ.get('CHANNELS', '-1001855754121').split()]
    FORCE_SUB = environ.get('FORCE_SUB','-1001787446188')
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and find.search(FORCE_SUB) else None
    FORCES_SUB_LINK = environ.get('FORCE_SUB_LINK','VJ_Bots')

    # Media Caption
    USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
    CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", Customize.FILE_CAPTION)

    # Filters Control
    FILTER_RESULTS = int(environ.get("FILTER_RESULTS", "5"))
    FILTER_BUTTONS = {}

    # Ads Controls
    WEB_URL = environ.get("MdiskLink.link")
    WEB_API = environ.get("a21d381121da4bae1dd61d5c7dc7ae8de52e6041")

    # other
    DONATE_LINKS = environ.get("DONATION_LINK", "https://t.me/+z5rBFKnY11JhZTY1")
    LOADING_SYMBOL = bool(environ.get("LOADING_MODE", True))
    LOADING_A = environ.get("LOADING_SYMBOL_A", "??????")
    LOADING_B = environ.get("LOADING_SYMBOL_B", "??????")
    STOP_BOT = bool(environ.get("DEFAULT", False))
    PORT_CODE = environ.get("PORT", "8080")
    broadcast_ids = {} # don't change this..!!  

class Index(object):
    CURRENT = int(environ.get("SKIP", 2))
    CANCEL = False

# bot management 
async def bot_run():
    _app = web.Application(client_max_size=30000000)
    _app.add_routes(routes)
    return _app

# class Settings(object):
#     IMDB_POSTER = False / "off"
#     WELCOME = True / "on"
#     BUTTON_SIZE = False / "off"
#     SPELLCHECK = True / "off"
#     FILE_MODE = False / "callback"
