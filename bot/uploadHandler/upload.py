import logging as LOGGER
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
import urllib.parse
from requests.utils import requote_uri

from googleapiclient.errors import HttpError

from bot.drivefunc.gdriveUpload import mydrive
from bot.util.utils import Human_size
from tpool.pool import run_in_thread


async def upload_handler(file_path, sentm):
    user_id = str(sentm.chat.id)
    try:
        _uploadedFile = await __finalUpload(file_path, user_id)
        download_button = InlineKeyboardMarkup([
            [InlineKeyboardButton(
                "Download", url=f"https://drive.google.com/open?id={_uploadedFile['id']}")],
            [InlineKeyboardButton(
                "Index link", url= requote_uri(f"https://www.suup.workers.dev/0:/{_uploadedFile['title']}"))],
            [InlineKeyboardButton(
                "Delete permanent",callback_data=f"delete||{_uploadedFile['id']}" )],
            [InlineKeyboardButton(
                "Move To Trash", callback_data=f"trash||{_uploadedFile['id']}")],
        ])
        await sentm.edit(f"Filename: `{_uploadedFile['title']}`\nSize: `{Human_size(_uploadedFile['fileSize'])}`", reply_markup=download_button)
    except HttpError as e:
        LOGGER.error(e)
        await sentm.edit(e._get_reason())
    except Exception as e:
        LOGGER.error(e)
        await sentm.edit(f"`{e}`\n#error")
    finally:
        os.remove(file_path)
        LOGGER.info("file Removed from disk")


@run_in_thread
def __finalUpload(file_path, user_id):
    if os.path.isdir(file_path):
        LOGGER.info(" Folder upload Init.. (not implemented lel)")
        pass
    if os.path.isfile(file_path):
        dr = mydrive(user_id)
        return dr.upload(file_path)
