from aiogram import types
from bot_utils import get_lp_holders_by_contract
from data.config import lp_contracts

async def holders(msg: types.Message):
    text = msg.text.split(" ")
    if len(text) > 1:
        data = None

        if text[1].lower() in lp_contracts:
            if len(text) > 2:
                if text[2].isdigit():
                    if int(text[2]) > 50:
                        await msg.answer("Превышен лимит :(")
                        return
                    if int(text[2]) < 1:
                        await msg.answer("Нельзя посмотреть меньше одного холдера :(")
                        return

                    data = await get_lp_holders_by_contract(lp_contracts[text[1].lower()], int(text[2]))
                else:
                    await msg.answer("Введённый лимит не является числом!")
                    return
            else:
                data = await get_lp_holders_by_contract(lp_contracts[text[1].lower()])
        
            holders = "\n".join(f"<code>{i}: {data[i]} LP</code>" for i in data)
            
            if holders != "":
                await msg.answer(f"""
<b>Информация о холдерах {text[1].upper()}-LP токенов</b>

{holders}

<b>ЕСЛИ ВЫ ЗАМЕТИЛИ СВОЙ АДРЕС В ЭТОМ СПИСКЕ - ВЫВОДИТЕ ЛИКВИДНОСТЬ С v1.dedust.io!</b>
""", parse_mode="html")
            
            else:
                await msg.answer("Холдеров LP-токена нету :)")


        else:
            await msg.answer("Данный токен не обнаружен в нашей базе!")
    
    else:
        await msg.answer("Недостаточно аргументов!")
