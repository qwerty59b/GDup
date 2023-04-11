# from pyrogram import Client

async def inChannel(client,message):
        try: 
            await client.get_chat_member("aca pon el nombre de usuario del canal sin @", message.from_user.id)
            print("in channel")
            return True
        except Exception as e:
            print("not a member")
            return False
