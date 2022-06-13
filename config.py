## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAAYtl8llSdMaZBA69Sw72tVSag5LNfPaG17bSbPMZjoIygHkoKkEXzB1orMeoYeuT5fgHony1RvqNug2gVCkkmAAep7BP-GgUwrRkZxS37qQeZe3MMohtVD4QffuwyqREHcZvhqMV8UwKdxg3DcKOeewuVxtFepHFevd8UrE8YzhoTdrTLEE-3pFoMK9Fh7EQvhlPcli_lVStCBkV8qiUQ7FLEGZVzEHKj3Cl3pPClazzcsZv_EiQ2s_rlcxdZZ4yU9D-RefK-CuWQsL0FiXH9KQQeakM5NLoOYWjElcB-Utwmn-Opry6rRJd9_66_XH-LIlQDpxGi8fToCfD46a8MwAAAAAUCtdZ8A")
BOT_TOKEN = getenv("BOT_TOKEN", "5353641392:AAHrG7uci02NtS_sxbbj_NCUrhUV4yAyTPg")
BOT_NAME = getenv("BOT_NAME", "Tom bot")
API_ID = int(getenv("API_ID", "9157919"))
API_HASH = getenv("API_HASH", "b90c282e584222babde5f68b5b63ee3b")
OWNER_NAME = getenv("OWNER_NAME", "Tom")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Tom_01157")
ALIVE_NAME = getenv("ALIVE_NAME", "Tom")
BOT_USERNAME = getenv("BOT_USERNAME", "Tom01212bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Ahmed1157")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "kyoga1")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Tom01255")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5352754419").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
