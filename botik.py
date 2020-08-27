from teleconfig import token
from telegram.ext import Updater, CommandHandler
from datetime import date

cp77date = date(2020, 11, 19)

def hello(update, context):
    update.message.reply_text(
        'Hello, {}'.format(update.message.from_user.first_name))

def cp77(update, context):
    update.message.reply_text(
        
        'CP77 выйдет {}'.format(cp77date)
    )





updater = Updater(token, use_context=True)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('cp77', cp77))

updater.start_polling()
updater.idle()
