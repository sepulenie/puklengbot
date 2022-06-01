import sqlite3, random

conn = sqlite3.connect("dickdump.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE  IF NOT EXISTS   dickdump(chat_id integer, word_0 text, word_1 text)""")


def make_pairs(words_in_message):
    for i in range(len(words_in_message)- 1):
            yield (words_in_message[i], words_in_message[i + 1])


def add_word_to_dictionary(words_in_message, chat_id):
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

def markov_generator(message):
    print(message)