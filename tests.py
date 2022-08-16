import random, sqlite3, logging, urllib3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from teleconfig import token
from generator import add_words_in_message_to_dictionary, generate_message, zachem, beestickers
logging.basicConfig(filename='bot.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

https = urllib3.PoolManager()
conn = sqlite3.connect("dickdump_test.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS dickdump(chat_id integer, word_0 text, word_1 text, is_first integer)""")
conn.commit()