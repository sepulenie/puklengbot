'''
ver. 0.4.1
'''
import random, sqlite3, logging, urllib3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from teleconfig import token
from generator import add_words_in_message_to_dictionary, generate_message, zachem, beestickers
logging.basicConfig(filename='bot.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

https = urllib3.PoolManager()
conn = sqlite3.connect("dickdump.db", check_same_thread=False)
conn2 = sqlite3.connect("chatsconfig.db", check_same_thread=False)
cursor = conn.cursor()
cursor2 = conn2.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS dickdump(chat_id integer, word_0 text, word_1 text, is_first integer)""")
cursor2.execute("""CREATE TABLE IF NOT EXISTS chatsconfig(chat_id integer, yauheni_enabled integer, shitpost_chance integer)""")
conn.commit()
conn2.commit()

get_all_chats = "SELECT * FROM chatsconfig"
cursor2.execute(get_all_chats)
all_chats_fetch = (cursor2.fetchall())
all_chat_ids = [row[0] for row in all_chats_fetch]
all_yauhenis_statuses = [row[1] for row in all_chats_fetch]
all_chances = [row[2] for row in all_chats_fetch]


def start(update, context):
    context.bot.send_message(chat_id = update.effective_message.chat_id, text = "Привет")


def start_shitpost(update, context):
    chat_id = update.effective_message.chat.id
    if chat_id in all_chat_ids:
        if all_yauhenis_statuses[all_chat_ids.index(chat_id)] == 0:
            cursor2.execute("UPDATE chatsconfig SET yauheni_enabled=? WHERE chat_id=?", (1, chat_id))
            all_yauhenis_statuses.insert(all_chat_ids.index(chat_id), 1)
            context.bot.send_message(chat_id = update.effective_message.chat_id, text = "Стартую...")
        else:
            context.bot.send_message(chat_id = update.effective_message.chat_id, text = "Я уже начал...")
    else:
        cursor2.execute("INSERT INTO chatsconfig VALUES (?,?,?)", (chat_id, 1, 1))
        all_chat_ids.append(chat_id)
        all_yauhenis_statuses.append(1)
        all_chances.append(1)
        context.bot.send_message(chat_id = update.effective_message.chat_id, text = "Стартую...")
    conn2.commit()


def stop_shitpost(update, context):
    chat_id = update.effective_message.chat.id
    if chat_id in all_chat_ids:
        if all_yauhenis_statuses[all_chat_ids.index(chat_id)] == 1:
            cursor2.execute("UPDATE chatsconfig SET yauheni_enabled=? WHERE chat_id=?", (0, chat_id))
            all_yauhenis_statuses.insert(all_chat_ids.index(chat_id), 0)
            context.bot.send_message(chat_id = update.effective_message.chat_id, text = "Приостанавливаю щитпост...")
        else:
            context.bot.send_message(chat_id = update.effective_message.chat_id, text = "Я и не стартовал...")
    else:
        cursor2.execute("INSERT INTO chatsconfig VALUES (?,?,?)", (chat_id, 0, 1))
        all_chat_ids.append(chat_id)
        all_yauhenis_statuses.append(0)
        all_chances.append(0)
        context.bot.send_message(chat_id = update.effective_message.chat_id, text = "Приостанавливаю щитпост...")
    conn2.commit()


def power(update, context):
    chat_id = update.effective_message.chat.id
    if chat_id in all_chat_ids:
        try:
            shitpost_chance = int(context.args[0])
            if shitpost_chance >= 1 and shitpost_chance <= 1000:
                all_chances.insert(all_chat_ids.index(chat_id), shitpost_chance)
                cursor2.execute("UPDATE chatsconfig SET shitpost_chance=? WHERE chat_id=?", (shitpost_chance, chat_id))
                context.bot.send_message(chat_id = update.effective_message.chat_id, text = "Устанавливаю силу щитпоста")
            else: 
                context.bot.send_message(chat_id = update.effective_message.chat_id, text = "Что-то не то, надо заново (от 1 до 1000)")
        except (IndexError, ValueError):
            context.bot.send_message(chat_id = update.effective_message.chat_id, text = "Что-то не то, надо заново (от 1 до 1000)")
    else:
        pass
    conn2.commit()


def message_handler(update, context):
    chat_id = update.effective_message.chat.id
    message = update.effective_message.text or update.effective_message.caption
    if chat_id in all_chat_ids and all_yauhenis_statuses[all_chat_ids.index(chat_id)]:
        add_words_in_message_to_dictionary(message, chat_id)
        d = int(2000*random.random())
        if d < (all_chances[all_chat_ids.index(chat_id)]) or (update.effective_message.reply_to_message != None and update.effective_message.reply_to_message.from_user.username == "puklengtime_bot"):
            context.bot.send_message(chat_id = update.effective_message.chat_id, text = generate_message(message, chat_id))
        else:
            pass
    if message.lower().startswith(zachem) or message.lower().endswith(zachem):
        update.message.reply_sticker(random.choice(beestickers))
    else:
        pass


def ment(update, context):
    update.message.reply_text('Здравия желаю!')


def main():
    updater = Updater(token, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', start)) #создает базу словаря
    updater.dispatcher.add_handler(CommandHandler('start_shitpost', start_shitpost)) #начать щитпостить
    updater.dispatcher.add_handler(CommandHandler('stop_shitpost', stop_shitpost)) #остановить щитпост
    updater.dispatcher.add_handler(CommandHandler('power', power)) #установить силу щитпоста
    updater.dispatcher.add_handler(MessageHandler((Filters.text | Filters.caption) & (~Filters.command | ~Filters.forwarded), message_handler)) #обрабатывает сообщение
    updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, ment)) # приветствие при добавлении в чат
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
