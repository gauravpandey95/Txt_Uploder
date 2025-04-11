import os

API_ID = API_ID = 29946578

API_HASH = os.environ.get("API_HASH", "57e0b762f105ab1db072fabe4d65114b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7671869618:AAEplVu9irkVnMbc6gCfj_7xJ65wjPhksWA")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6376631545))

LOG = -1002378050154

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6376631545").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


