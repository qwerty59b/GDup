from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
async def sendJoinmsg(message):
    joinButton=InlineKeyboardMarkup([  
        
        [InlineKeyboardButton("Join", url="https://t.me/zzzzzzzpromax1")]  
    
    ])
    await message.reply_text("join channel To access Bot 🔐 " ,reply_markup = joinButton)
