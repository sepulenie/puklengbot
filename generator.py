import sqlite3, random, re

conn = sqlite3.connect("dickdump.db", check_same_thread=False)
cursor = conn.cursor()

def add_words_in_message_to_dictionary(message, chat_id):
    message = re.sub(r"http\S+", " ", message)
    message = re.sub(r"\S*@\S*\s?", " ", message)
    message = re.sub(r"\n", " ", message)
    words_in_message = message.split(" ")
    print(words_in_message)
    def make_pairs(words_in_message):
        for i in range(len(words_in_message)- 1):
            yield (words_in_message[i], words_in_message[i + 1])

    pair_of_words = make_pairs(words_in_message)
    print(pair_of_words)

    for word_0, word_1 in pair_of_words:
        search = "SELECT * FROM dickdump WHERE chat_id=? AND word_0=?"
        cursor.execute(search, [(chat_id), (word_0)])
        search_result = (cursor.fetchone())
        if search_result == None:
            cursor.execute("INSERT INTO dickdump VALUES (?,?,?)", (chat_id, word_0, repr({word_1: 1})))
        else:
            search_result_word_0 = search_result[1]
            search_result_word_1 = dict
            search_result_word_1 = eval(search_result[2])
            if word_1 in search_result_word_1.keys():
                search_result_word_1.update({word_1: (search_result_word_1.get(word_1)+1)})
                print(search_result_word_1)
                cursor.execute("UPDATE dickdump SET word_1=? WHERE word_0=?", (repr(search_result_word_1), search_result_word_0))
            else:
                search_result_word_1.update({word_1:1})
                cursor.execute("UPDATE dickdump SET word_1=? WHERE word_0=?", (repr(search_result_word_1), search_result_word_0))
    conn.commit()

def generate_shitpost(message, chat_id):
    print("hello")





'''
def next_word(first_word, chat_id):
    search = "SELECT word_1 FROM dickdump WHERE chat_id=? AND word_0=?"
    cursor.execute(search, [(chat_id), (first_word)])
    search_result = (cursor.fetchone())
    if search_result == None:
        return None
    else:
        search_result_word_1 = random.choice(eval(search_result[0]))
        return(search_result_word_1)


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
'''
