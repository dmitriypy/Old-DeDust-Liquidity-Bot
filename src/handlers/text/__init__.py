from aiogram import Dispatcher

from handlers.text.start import bot_start
from handlers.text.liquidity_info import liquidity
from handlers.text.lp_holders import holders

def register_user_handler(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])

    dp.register_message_handler(liquidity, commands=['liquidity'])
    dp.register_message_handler(holders, commands=['holders'])