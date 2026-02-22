from .. import loader, utils 
from telethon import events 
from telethon.errors.rpcerrorlist import YouBlockedUserError 
from asyncio.exceptions import TimeoutError 
 
 
def register(cb): 
    cb(ErrorMod()) 
 
class ErrorMod(loader.Module): 
    """Модуль для проверки слов на наличие ошибок """ 
    strings = {'name': 'Пиши грамотно'} 
 
    async def errcmd(self, message): 
        """Пиши .err + слово, можно реплай.""" 
        try: 
            text = utils.get_args_raw(message) 
            reply = await message.get_reply_message() 
            chat = "@SpellingMasterBot" 
            if not text and not reply: 
                await message.edit("<b>А аргументы кто указывать будет</b>") 
                return 
            if text: 
                await message.edit("<b>уну моменто</b>") 
                async with message.client.conversation(chat) as conv: 
                    try: 
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=1037534015)) 
                        await message.client.send_message(chat, text) 
                        response = await response 
                    except YouBlockedUserError: 
                        await message.reply("<b>Удали из ЧС: @SpellingMasterBot</b>") 
                        return 
                    if not response.text: 
                        await message.edit("<Ещё раз пробуй</b>") 
                        return 
                    await message.delete() 
                    await message.client.send_message(message.to_id, response.text) 
            if reply: 
                await message.edit("<b>Секундочку</b>") 
                async with message.client.conversation(chat) as conv: 
                    try: 
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=1037534015)) 
                        await message.client.send_message(chat, reply) 
                        response = await response 
                    except YouBlockedUserError: 
                        await message.reply("<b>Удали из ЧС: @SpellingMasterBot</b>") 
                        return 
                    if not response.text: 
                        await message.edit("<Пробуй еще раз </b>") 
                        return 
                    await message.delete() 
                    await message.client.send_message(message.to_id, response.text) 
        except TimeoutError: 
            return await message.edit("<b>Неизвестная ошибка</b>")
