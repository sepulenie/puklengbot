import datetime
from teleconfig import token
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def hello(update, context):
    update.message.reply_text(
        'Hello, {},\nмы находимся в чате под названием "{}"'.format(update.message.from_user.first_name, update.message.chat.title))

def echo(update,context):
    a = update.message.text.lower()
    if a == 'да':
        print ('да')
        update.message.reply_text('Пизда')
    
def sun(update, context):
    print('member joined')
    update.message.reply_text('Под этим солнцем и небом мы тепло приветствуем тебя!')

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
    print(result)

    update.message.reply_text(
        result
    )





def main():
    updater = Updater(token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('cp77', cp77))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, sun))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()