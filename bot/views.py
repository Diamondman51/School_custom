# from django.shortcuts import render
import json
from rest_framework.views import View
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from . import config

# Create your views here.

bot = Bot(
    token=config.BOT_TOKEN,
    # session=session,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

HOOK = '/hook'
HOOK_URL = f'https://318c-104-154-169-9.ngrok-free.app/bot{HOOK}'

storage = MemoryStorage()

dp = Dispatcher(
    storage=storage,
)


class BotView(View):
    async def post(self, request):
        
        data = await json.loads(request.body)
        update = Update(**data)
        await dp.feed_update(bot=bot, update=update)
        return {'update': 'True'}
    

class SetHook(View):
    async def get(self):
        await bot.set_webhook(HOOK_URL)
        return {'hook': True}

    @classmethod
    async def start(cls):
        await cls.get(cls)

class DeleteHook(View):
    async def get(self):
        await bot.delete_webhook()
        return {'hook': False}
