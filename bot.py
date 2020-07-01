import logging
import os

from aioviber.bot import Bot
from aioviber.chat import Chat
from viberbot.api.viber_requests import ViberSubscribedRequest

logger = logging.getLogger(__name__)

ENV = True

if ENV:
    BOT_NAME = os.environ.get('BOT_NAME', None)
    AVATAR_URL = os.environ.get('AVATAR_URL', None)
    AUTH_TOKEN = os.environ.get('AUTH_TOKEN', None)
    HOST_NAME = os.environ.get('HOST_NAME', None)
    WEBHOOK = os.environ.get('WEBHOOK', None)

bot = Bot(
    name=BOT_NAME,
    avatar=AVATAR_URL,
    auth_token=AUTH_TOKEN,  # Public account auth token
    host=HOST_NAME,  # should be available from wide area network
    port=80,
    webhook=WEBHOOK,  # Webhook url
)

@bot.command('ping')
async def ping(chat: Chat, matched):
    await chat.send_text('pong')

@bot.command('start')
async def start(chat: Chat, matched):
    await chat.send_text('Im Alive! I was created on purpose of being a Chatbot, My master is Aman')

@bot.event_handler('subscribed')
async def user_subscribed(chat: Chat, request: ViberSubscribedRequest):
    await chat.send_text('Welcome')

@bot.message_handler('sticker')
async def sticker(chat: Chat):
    await chat.send_sticker(5900)

if __name__ == '__main__':  # pragma: no branch
    await bot.run()  # pragma: no cover