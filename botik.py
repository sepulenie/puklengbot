'''
ver. 0.1.6 dic
'''
import random, sqlite3, logging, urllib3, re
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from teleconfig import token
from generator import add_words_in_message_to_dictionary, generate_shitpost
logging.basicConfig(filename='bot.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

https = urllib3.PoolManager()
conn = sqlite3.connect("dickdump.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS dickdump(chat_id integer, word_0 text, word_1 text)""")
conn.commit()
markov_chance = 100


def start(update):
    chat_id = update.message.chat.id
    update.message.reply_text('ID чата - ', chat_id)
    cursor.execute("INSERT INTO dickdump VALUES (?,?,?)", (chat_id, "Добрый", repr({"День": 1})))
    conn.commit()

def message_handler(update, context):
    chat_id = update.message.chat.id
    message = update.message.text
    print("\nИзначальное сообщение -- ", message, "\n")
    add_words_in_message_to_dictionary(message, chat_id)
    if random.random() < markov_chance/100 or (update.message.reply_to_message != "None" and update.message.reply_to_message.from_user.username == "puklengtime_bot"):
        generate_shitpost('message', chat_id)
    else:
        pass
    

def main():
    updater = Updater(token, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', start)) #создает базу словаря
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler)) #добавляет слово из чата в словарь
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()