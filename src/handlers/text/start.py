from aiogram import types


async def bot_start(msg: types.Message):
    await msg.answer("""
Привет! Я создан для того, чтобы показывать тебе информацию о токенах, которые находились на v1.dedust.io.

Вот мои команды:
/liquidity <symbol> - получить информацию о ликвидности токена
/holders <symbol> <limit> - получить информацию о холдерах LP токена
""")