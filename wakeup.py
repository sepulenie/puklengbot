import sqlite3, random

conn = sqlite3.connect("dickdump.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE  IF NOT EXISTS   dickdump(word_1 text, word_2 text)""")


message = 'Одна рыба две рыбы три'


def next_word(first_word):
    search = "SELECT * WHERE word_1=?"
    cursor.execute(search, [first_word])
    search_result = (cursor.fetchone())

def markov(message):
        message_split = message.split()
        first_word = random.choice(message_split)
        print(first_word)
        chain = [first_word]
        n_words = random.randint(1, 60)
        next_word(first_word)

#markov(message)






'''
def markov(update, context):
    dickdict = {}
    for key, val in csv.reader(open('dickdump.csv')):
        dickdict[key] = val
    first_word = random.choice(list(dickdict.keys()))
    print(dickdict)
    while first_word[0].isupper() == False:
        first_word = random.choice(list(dickdict.keys()))
    else:
        chain = [first_word]
        n_words = random.randint(1, 30)
        first_word = random.choice(list(dickdict.keys()))
        for i in range(n_words):
            chain.append(random.choice(dickdict[chain[-i]]))
        markov_result = (' '.join(chain))
        update.message.reply_text(markov_result.replace(' , ', ', ').replace(' . ','. ').replace(' -','-'))
        '''