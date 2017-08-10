from flask import Flask, request

from telegram.ext import CommandHandler, MessageHandler, Filters, Dispatcher
from telegram import Bot, Update
import os, logging


# Load environment variables
TOKEN = os.environ.get('TOKEN')
BROADCAST_ID = os.environ.get('BROADCAST_ID')


app = Flask(__name__)
bot = Bot(TOKEN)
dp = Dispatcher(bot, None)

# Setup logging
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


from .util import txt
from .commands import random, b64, fortune, randint, randsample, uuid



# Broadcast a message to a channel or a person
if BROADCAST_ID:
    def echo(bot, update):
        bot.send_message(chat_id=BROADCAST_ID,
                         text='{} {}({}, from {}, @{}): \n{}'.format(
                             update.message.from_user.first_name,
                             update.message.from_user.last_name,
                             update.message.from_user.id,
                             update.message.chat_id,
                             update.message.from_user.username,
                             update.message.text
                         ))
        # Broadcast messages to channel
        dp.add_handler(MessageHandler(Filters.all, echo), 1)


handlers = [
    CommandHandler('start', txt('start.txt')),
    CommandHandler('help', txt('help.txt')),
    CommandHandler('random', random, pass_args=True),
    CommandHandler('b64', b64, pass_args=True),
    CommandHandler('fortune', fortune, pass_args=True),
    CommandHandler('randint', randint, pass_args=True),
    CommandHandler('randsample', randsample, pass_args=True),
    CommandHandler('uuid', uuid),
]

for h in handlers:
    dp.add_handler(h)


@app.route('/bot' + TOKEN, methods=['POST'])
def telegram_bot():
    if request.method == 'POST':
        update = Update.de_json(request.get_json(force=True), bot)
        dp.process_update(update)
        return 'Thanks!'


import maomihzbot.views
