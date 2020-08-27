
'''
def gettime():
    pukdate = date(2019, 4, 15)
    puktime = time(17, 00)
    pukdatetime = datetime.combine(pukdate, puktime)
    currenttime = datetime.now()
    ostatok = pukdatetime - currenttime
    secondstotal = ostatok.total_seconds()
    secs = timedelta(seconds=secondstotal)
    d = datetime(1,1,1) + secs
    pri = '{} часов {} минут {} секунд до разрыва пукленгов'.format(d.strftime("%H"), d.strftime("%M"), d.strftime("%S"))
    print(pri)
    return pri
    
   
bot = telebot.TeleBot(config.token)
@bot.message_handler(commands=['time'])

def sendtime_of_puklings(message):
    bot.send_message(message.chat.id, gettime())

@bot.message_handler(commands=["kikich"])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Оггоооо", url="www.goat.se")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Посмотри чем занимается кикич в свободное время :thinking:", reply_markup=keyboard)

@bot.message_handler(content_types=['new_chat_members'])
def handle_new_chat_member(message):
    bot.send_message(message.chat.id, "Петух бля приперся")

@bot.message_handler(commands=["roma"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button1 = types.InlineKeyboardButton(text="Поднять", callback_data="podnat")
    callback_button2 = types.InlineKeyboardButton(text="Перешагнуть", callback_data="pereshag")
    keyboard.add(callback_button1)
    keyboard.add(callback_button2)
    bot.send_message(message.chat.id, "Кидаю тебе под ноги полотенце", reply_markup=keyboard)





# В большинстве случаев целесообразно разбить этот хэндлер на несколько маленьких
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "podnat":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Кинул новичку полотенце, он его поднял и оказался норм ")
        if call.data == "pereshag":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Кинул новичку полотенце, он через него перешагнул")


if __name__ == '__main__':
    bot.polling(none_stop=True)

            
if __name__ == '__main__':
    bot.polling(none_stop=True)
'''