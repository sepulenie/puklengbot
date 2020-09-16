import sqlite3, random

conn = sqlite3.connect("dickdump.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE  IF NOT EXISTS   dickdump(word_1 text, word_2 text)""")


message = 'и за ним пошла одна или две, но всё же'


def next_word(first_word):
    search = "SELECT word_2 FROM dickdump WHERE word_1=?"
    cursor.execute(search, [(first_word)])
    search_result = (cursor.fetchone())
    print('список возможных слов - ', search_result)
    while search_result == None:
        return 'None'
    
    search_result = random.choice(search_result[0].split(','))
    print('следующее слово - ', search_result)
    return search_result



message = message.replace(',', ' , ').replace('.',' . ').replace('-',' - ').replace('?',' ? ').replace('!',' ! ').replace('«',' « ').replace('»',' » ').replace(';',' ; ')
words_in_message = message.split()
first_word = random.choice(words_in_message)
while first_word.isalpha() == False:
    first_word = random.choice(words_in_message)
else:
    print('первое слово - ', first_word)
    pass
chain = [first_word]

next_word_var = next_word(first_word)
chain.append(next_word_var)
first_word = next_word_var
print('получилось - ', chain)

'''
n_words = 5

for n in range(n_words):
    next_word_var = next_word(first_word)
    chain.append(next_word_var)
    first_word = next_word_var

print(' '.join(chain).replace(' , ', ', ').replace(' . ','. ').replace(' - ','-').replace(' ? ','? ').replace(' ! ','! ').replace(' ; ','; '))
'''












'''
for row in cursor.execute("SELECT * FROM dickdump"):
   split = row
   print(split)
'''



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