'''
ver. 0.1.4 test
'''
import random, sqlite3, logging, urllib3, re
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from teleconfig import token

logging.basicConfig(filename='bot.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

https = urllib3.PoolManager()
dog_url = https.request('GET','https://media.giphy.com/media/F65M9crzsQe2U3TpaI/giphy.gif')
kubik_path = r"/home/ubuntu/botfiles/puklengbot/kubik/"
markov_chance = 100
dick = {}
conn = sqlite3.connect("dickdump.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS dickdump(chat_id integer, word_0 text, word_1 text)""")


def start(update, context):
    chat_id = update.message.chat.id
    update.message.reply_text(chat_id)
    cursor.execute("INSERT INTO dickdump VALUES (?,?,?)", (chat_id, 'Добрый', repr(['день'])))


def make_pairs(words_in_message):
    for i in range(len(words_in_message)- 1):
            yield (words_in_message[i], words_in_message[i + 1])


def add_to_dick(words_in_message, chat_id):
    pair_of_words = make_pairs(words_in_message)
    for word_0, word_1 in pair_of_words:
        search = "SELECT * FROM dickdump WHERE chat_id=? AND word_0=?"
        cursor.execute(search, [(chat_id), (word_0)])
        search_result = (cursor.fetchone())
        if search_result == None:
            cursor.execute("INSERT INTO dickdump VALUES (?,?,?)", (chat_id, word_0, repr([word_1])))
        else:
            search_result_word_0 = search_result[1]
            search_result_word_1 = eval(search_result[2])
            if word_1 in search_result_word_1:
                pass
            else:
                search_result_word_1.append(word_1)
                cursor.execute("UPDATE dickdump SET word_1=? WHERE word_0=?", (repr(search_result_word_1), search_result_word_0))
    conn.commit()


def next_word(first_word, chat_id):
    search = "SELECT word_1 FROM dickdump WHERE chat_id=? AND word_0=?"
    cursor.execute(search, [(chat_id), (first_word)])
    search_result = (cursor.fetchone())
    if search_result == None:
        return None
    else:
        search_result_word_1 = random.choice(eval(search_result[0]))
        return(search_result_word_1)


def message_handler(update, context):
    message = re.sub(r"http\S+", "", update.message.text)
    message = re.sub(r"\S*@\S*\s?", "", message)
    message = message.replace('?!',' ?! ').replace('??',' ?? ').replace('!!',' !! ').replace('...',' ... ').replace(',', ' , ').replace('.',' . ').replace('-',' - ').replace('?',' ? ').replace('!',' ! ').replace('«',' « ').replace('»',' » ').replace(';',' ; ')
    words_in_message = message.split()
    chat_id = update.message.chat.id
    add_to_dick(words_in_message, chat_id)
    if random.random() < markov_chance/100 or (update.message.reply_to_message != "None" and update.message.reply_to_message.from_user.username == "puklengtime_bot"):
        random_index = random.randrange(0, (len(words_in_message)))
        first_word = words_in_message[random_index]
        while first_word.isalpha() == False:
            words_in_message.pop(random_index)
            random_index = random.randrange(0, (len(words_in_message)))
            first_word = words_in_message[random_index]
        chain = [first_word]
        next_word_var = next_word(first_word, chat_id)
        n_words = random.randint(2, 15)
        for i in range(n_words):
            next_word_var = next_word(first_word, chat_id)
            if next_word_var == None:
                pass
            else:
                chain.append(next_word_var)
                first_word = next_word_var
        exit_message = ' '.join(chain)
        exit_message = exit_message.replace(" ,", ", ").replace(" .",". ").replace(" -","-").replace(" ?","? ").replace(" !","! ").replace(" «","«").replace(" »","»").replace(" ;","; ").replace("  "," ")
        context.bot.send_message(chat_id = update.message.chat_id, text = exit_message)

def main():
    updater = Updater(token, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', start)) #создает базу словаря
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler)) #добавляет слово из чата в словарь
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()