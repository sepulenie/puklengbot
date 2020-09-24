import os, datetime, random, numpy, sqlite3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from teleconfig import token

kubik_path = r"/home/ubuntu/botfiles/puklengbot/kubik/"
# kubik_path = r"D:/Projects/Python/puklengbot/kubik/"

dick = {}
conn = sqlite3.connect("dickdump.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE  IF NOT EXISTS   dickdump(word_0 text, word_1 text)""")


def make_pairs(words_in_message):
    for i in range(len(words_in_message)- 1):
            yield (words_in_message[i], words_in_message[i + 1])

def add_to_dick(words_in_message):
    pair_of_words = make_pairs(words_in_message)
    for word_0, word_1 in pair_of_words:
        search = "SELECT * FROM dickdump WHERE word_0=?"
        cursor.execute(search, [(word_0)])
        search_result = (cursor.fetchone())
        if search_result == None:
            cursor.execute("INSERT INTO dickdump VALUES (?,?)", (word_0, repr([word_1])))
            #print(word_1, '- добавлено')
        else:
            search_result_word_0 = search_result[0]
            search_result_word_1 = eval(search_result[1])
            if word_1 in search_result_word_1:
                #print('слово {} уже в паре'.format(word_1))
                pass
            else:
                search_result_word_1.append(word_1)
                cursor.execute("UPDATE dickdump SET word_1=? WHERE word_0=?", (repr(search_result_word_1), search_result_word_0))
    conn.commit()

def message_handler(update, context):
    message = update.message.text.replace(',', ' , ').replace('.',' . ').replace('-',' - ').replace('?',' ? ').replace('!',' ! ').replace('«',' « ').replace('»',' » ').replace(';',' ; ')
    words_in_message = message.split()
    add_to_dick(words_in_message)








def hello(update, context):
    update.message.reply_text(
        'Hello, {},\nмы находимся в чате под названием "{}"'.format(update.message.from_user.first_name, update.message.chat.title))

def sun(update, context):
    update.message.reply_text('Под этим солнцем и небом мы тепло приветствуем тебя!')

def leave(update, context):
    update.message.reply_sticker("CAACAgIAAxkBAAEBRJRfSOutTFb77ZdoE6Fe4t09Sqi9cgACYAAD3N3lFSPHyb0-_G4ZGwQ")

#def pizda(update,context):
#   da = update.message.text.lower()
#   if da == 'да':
#       update.message.reply_text('Пизда')
#   elif da=='пизда':
#       update.message.reply_text('Да')
    
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

#def get_kub(update, context):
    #random_kubik = kubik_path + random.choice([kub for kub in os.listdir(kubik_path) if os.path.isfile(os.path.join(kubik_path, kub))])
    #update.message.reply_photo(photo = open(random_kubik , 'rb'))


def main():
    updater = Updater(token, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('hello', hello)) #говорит "привет"
    updater.dispatcher.add_handler(CommandHandler('cp77', cp77))    #отсчитывает время до cp77
    #updater.dispatcher.add_handler(CommandHandler('get_kub', get_kub)) # показать кубика из папки
    #updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, pizda)) #простейшее да-пизда
    updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, sun)) # приветствие при добавлении в чат
    updater.dispatcher.add_handler(MessageHandler(Filters.status_update.left_chat_member, leave)) # стикер при удалении из чата
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler)) #добавляет слово из чата в словарь
    #updater.dispatcher.add_handler(CommandHandler('markov', markov)) #говорит рандомную хуйню
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()