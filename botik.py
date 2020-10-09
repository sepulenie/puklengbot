'''
ver. 0.0.8
'''
import os, datetime, random, sqlite3, logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from teleconfig import token

logging.basicConfig(filename='bot.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


kubik_path = r"/home/ubuntu/botfiles/puklengbot/kubik/"
# kubik_path = r"D:/Projects/Python/puklengbot/kubik/"
markov_chance = 3
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
    message = update.message.text.replace(',', ' , ').replace('.',' . ').replace('-',' - ').replace('?',' ? ').replace('!',' ! ').replace('«',' « ').replace('»',' » ').replace(';',' ; ')
    words_in_message = message.split()
    chat_id = update.message.chat.id
    add_to_dick(words_in_message, chat_id)
    if random.random() < markov_chance/100:
        random_index = random.randrange(0, (len(words_in_message)))
        first_word = words_in_message[random_index]
        while first_word.isalpha() == False:
            words_in_message.pop(random_index)
            random_index = random.randrange(0, (len(words_in_message)))
            first_word = words_in_message[random_index]
        chain = [first_word]
        next_word_var = next_word(first_word, chat_id)
        n_words = random.randint(1, 30)
        for i in range(n_words):
            next_word_var = next_word(first_word, chat_id)
            if next_word_var == None:
                pass
            else:
                chain.append(next_word_var)
                first_word = next_word_var
        exit_message = ' '.join(chain)
        exit_message = exit_message.replace(" ,", ", ").replace(" .",". ").replace(" -"," - ").replace(" ?","? ").replace(" !","! ").replace(" «","«").replace(" »","»").replace(" ;","; ").replace("  "," ")
        update.message.reply_text(exit_message)

def hello(update, context):
    update.message.reply_text(
        'Hello, {},\nмы находимся в чате под названием "{}"'.format(update.message.from_user.first_name, update.message.chat.title))




def sun(update, context):
    update.message.reply_text('Под этим солнцем и небом мы тепло приветствуем тебя!')


def leave(update, context):
    update.message.reply_sticker("CAACAgIAAxkBAAEBRJRfSOutTFb77ZdoE6Fe4t09Sqi9cgACYAAD3N3lFSPHyb0-_G4ZGwQ")


def cp77(update, context):
    def truedays(days):
        day = str(days)
        if day[-1] in ['0', '5', '6', '7', '8', '9'] or (len(day) > 1 and day[-2] == '1'):
            return '{0} дней'.format(day)
        elif day[-1] in ['2', '3', '4'] or (len(day) > 1 and day[-2] == '1'):
            return '{0} дня'.format(day)
        elif day[-1] == '1':
            return '{0} день'.format(day)

    def truehours(hours):
        hour = str(hours)
        if hour[-1] in ['0', '5', '6', '7', '8', '9'] or (len(hour) > 1 and hour[-2] == '1'):
            return '{0} часов'.format(hour)
        elif hour[-1] in ['2', '3', '4'] or (len(hour) > 1 and hour[-2] == '1'):
            return '{0} часа'.format(hour)
        elif hour[-1] == '1':
            return '{0} час'.format(hour)

    def trueminutes(minutes):
        minute = str(minutes)
        if minute[-1] in ['0', '5', '6', '7', '8', '9'] or (len(minute) > 1 and minute[-2] == '1'):
            return '{0} минут'.format(minute)
        elif minute[-1] in ['2', '3', '4'] or (len(minute) > 1 and minute[-2] == '1'):
            return '{0} минуты'.format(minute)
        elif minute[-1] == '1':
            return '{0} минута'.format(minute)
            
    currentdatetime = datetime.datetime.now()
    itsready = datetime.datetime(2020, 11, 19, 0, 0)
    whenitsready = (itsready - currentdatetime)
    td = truedays(whenitsready.days)
    th = truehours(whenitsready.seconds//3600)
    tm = trueminutes((whenitsready.seconds//60) % 60)
    result = "до выхода Cyberpunk 2077 осталось: {0}, {1}, {2}".format(td, th, tm)
    update.message.reply_text(result)

def get_kub(update, context):
    random_kubik = kubik_path + random.choice([kub for kub in os.listdir(kubik_path) if os.path.isfile(os.path.join(kubik_path, kub))])
    update.message.reply_photo(photo = open(random_kubik , 'rb'))


def main():
    updater = Updater(token, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('hello', hello)) #говорит "привет"
    updater.dispatcher.add_handler(CommandHandler('start', start)) #создает базу словаря
    updater.dispatcher.add_handler(CommandHandler('cp77', cp77))    #отсчитывает время до cp77
    updater.dispatcher.add_handler(CommandHandler('get_kub', get_kub)) # показать кубика из папки
    updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, sun)) # приветствие при добавлении в чат
    updater.dispatcher.add_handler(MessageHandler(Filters.status_update.left_chat_member, leave)) # стикер при удалении из чата
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler)) #добавляет слово из чата в словарь
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
