from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("9157919"))
API_HASH = getenv("b90c282e584222babde5f68b5b63ee3b")
BOT_TOKEN = getenv("5353641392:AAHrG7uci02NtS_sxbbj_NCUrhUV4yAyTPg")
SESSION_NAME = getenv("BAAuf_mrUum0Mg3JV3eB8d8Na2pFa2dvxT9aRGSlzGLTe5l_5T_V_sf3JzaZB_EqY8B1-j8tpMry6kSqB7QKPnrMwYebUyReRuYIASqLDESjtQL7aBIenCGRHygqrMZY7fd5GOVFfbK-WJNqCuuo6iy3iJAZHZf0HfJG1q9rcl-VQINzMVTvrY2JrsW70iFSd3ojsk6Cik3_hISwq51zoOSlqdu_Zwy4_Prb8HDIAngQCpr_RtxomB8XkM76dyG4Kdkyr1PuicyiKEHsDYDEN88mNCbfPePbbdWHuwwCJiUS2rSoBkoyBNNYCgVQ_ogyJFePm5oDevOsPG9IrfvQ43O_AAAAAT8MjPMA")

# mandatory vars
OWNER_USERNAME = getenv("Tom_01157")
ALIVE_NAME = getenv("Tom")
BOT_USERNAME = getenv("Tom01212bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/lMl10l/lMl10l")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "jepthonsupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Tom01255")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("mongodb+srv://hussein87:Hussein87@cluster0.wynpz.mongodb.net/?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
OWNER_ID = list(map(int, getenv("5352754419").split()))
SUDO_USERS = list(map(int, getenv("5352754419").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
