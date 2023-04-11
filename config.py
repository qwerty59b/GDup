import os

DOWNLOAD_LOCATION = "./Downloads"
BOT_TOKEN = os.environ.get("BOT_TOKEN", "aca va tu token con las comillas")
APP_ID = int(os.environ.get("API_ID", "aca va tu id con las comillas"))
API_HASH = os.environ.get("API_HASH", "aca va tu hash con las comillas")
AUTH_GROUP = "" #aca no pongas nada

Creds_path = "creds"
DOWNLOAD_LOCATION = "/"

adminList = [12345] #aca va el id de tg del administrador del bot y el canal


EDIT_TIME = 5
FINISHED_PROGRESS_STR = "*"
UNFINISHED_PROGRESS_STR = "_"
