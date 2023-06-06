from aiogram import types

from bot_utils import get_info_by_contract
from data.config import lp_contracts


async def liquidity(msg: types.Message):
    text = msg.text.split(" ")
    if len(text) > 1:
        if text[1].lower() in lp_contracts:
            data = await get_info_by_contract(lp_contracts[text[1].lower()])
            
            if data != []:
                await msg.answer(f"""
<b>Информация о ликвидности для ${text[1].upper()}</b>

TON Liquidity = {data[1]} TON
{text[1].upper()} Liquidity = {data[0]} {text[1].upper()}
""", parse_mode="html")

            else:
                await msg.answer("Вся ликвидность этого токена была выведена(возможно. советую посмотреть холдеров)")

        else:
            await msg.answer("Данный токен не обнаружен в нашей базе!")
    else:
        await msg.answer("Недостаточно аргументов!")