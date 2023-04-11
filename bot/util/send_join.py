from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
async def sendJoinmsg(message):
    joinButton=InlineKeyboardMarkup([  
        
        [InlineKeyboardButton("Join", url="link de tu canal con t.me/canalmio")]  
    
    ])
    await message.reply_text("join channel To access Bot 🔐 " ,reply_markup = joinButton)
