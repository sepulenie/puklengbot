import random, sqlite3, logging, urllib3
'''from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from teleconfig import token
from generator import add_words_in_message_to_dictionary, generate_message, zachem, beestickers
logging.basicConfig(filename='bot.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

https = urllib3.PoolManager()
conn = sqlite3.connect("dickdump.db", check_same_thread=False)
cursor = conn.cursor()
search = "SELECT * FROM dickdump WHERE chat_id=? AND word_0=? ORDER BY random()"
cursor.execute(search, [-1001410341144, "⚡"])
search_result = (cursor.fetchone())
first_word_in_sentence = search_result[1]
search = "SELECT word_1 FROM dickdump WHERE chat_id=? AND word_0=?"
cursor.execute(search, [(-1001410341144), (first_word_in_sentence)])
search_result = cursor.fetchone()
print(search_result)
'''

first_emoji = "1"
second_emoji = "2"
print(random.choice(first_emoji, second_emoji))