import sqlite3, random

conn = sqlite3.connect("dickdump.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE  IF NOT EXISTS   dickdump(word_0 text, word_1 text)""")
'''
for row in cursor.execute("SELECT * FROM dickdump"):
   split = row
   print(split)
'''

def next_word(first_word):
    search = "SELECT word_1 FROM dickdump WHERE word_0=?"
    cursor.execute(search, [(first_word)])
    search_result = (cursor.fetchone())
    if search_result == None:
        return None
    else:
        search_result_word_1 = random.choice(eval(search_result[0]))
        return(search_result_word_1)


message = 'одна рыба в нашей стране, по мне не нужна! Ну либо так либо не так потому что уходить в страну или выходить'
message = message.replace(',', ' , ').replace('.',' . ').replace('-',' - ').replace('?',' ? ').replace('!',' ! ').replace('«',' « ').replace('»',' » ').replace(';',' ; ')
words_in_message = message.split()
random_index = random.randrange(0, (len(words_in_message)-1))
first_word = words_in_message[random_index]

while first_word.isalpha() == False:
    words_in_message.pop(random_index)
    random_index = random.randrange(0, (len(words_in_message)-1))
    first_word = words_in_message[random_index]

chain = [first_word]
next_word_var = next_word(first_word)
n_words = 3
for i in range(5):
    next_word_var = next_word(first_word)
    if next_word_var == None:
        pass
    else:
        chain.append(next_word_var)
        first_word = next_word_var
exit_message = ' '.join(chain)
exit_message = exit_message.replace(" ,", ", ").replace(" .",". ").replace(" -","-").replace(" ?","? ").replace(" !","! ").replace(" «","«").replace(" »","»").replace(" ;","; ").replace("  "," ")
print(exit_message)



'''

next_word_var = next_word(first_word)
while next_word_var == None:
    words_in_message.pop(words_in_message.index(first_word))
    next_word_var = next_word(first_word)




chain.append(next_word_var)
first_word = next_word_var
print('получилось - ', chain)

n_words = 5

for n in range(n_words):
    next_word_var = next_word(first_word)
    chain.append(next_word_var)
    first_word = next_word_var

print(' '.join(chain).replace(' , ', ', ').replace(' . ','. ').replace(' - ','-').replace(' ? ','? ').replace(' ! ','! ').replace(' ; ','; '))
'''