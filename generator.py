import sqlite3, random, re

conn = sqlite3.connect("dickdump.db", check_same_thread=False)
cursor = conn.cursor()

def add_words_in_message_to_dictionary(message, chat_id):
    message = re.sub(r"http\S+", " ", message)
    message = re.sub(r"\S*@\S*\s?", " ", message)
    message = re.sub(r"\n", " ", message)
    words_in_message = message.split(" ")
    def make_pairs(words_in_message):
        for i in range(len(words_in_message)- 1):
            yield (words_in_message[i], words_in_message[i + 1])

    pair_of_words = make_pairs(words_in_message)

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
                #print(search_result_word_1)
                cursor.execute("UPDATE dickdump SET word_1=? WHERE word_0=?", (repr(search_result_word_1), search_result_word_0))
            else:
                search_result_word_1.update({word_1:1})
                cursor.execute("UPDATE dickdump SET word_1=? WHERE word_0=?", (repr(search_result_word_1), search_result_word_0))
    conn.commit()


def select_next_word(first_word, chat_id):
    print("Ищем слово в словаре")
    search = "SELECT word_1 FROM dickdump WHERE chat_id=? AND word_0=?"
    cursor.execute(search, [(chat_id), (first_word)])
    search_result = (cursor.fetchone())
    print(search_result)
    if search_result == None:
        return None
    else:
        search_result_for_next_word = random.choice(eval(search_result[0]))
        print(search_result_for_next_word)
        return(search_result_for_next_word)


def generate_message(message, chat_id):
    print('Начинаем генерировать ответ...')
    message = re.sub(r"http\S+", " ", message)
    message = re.sub(r"\S*@\S*\s?", " ", message)
    message = re.sub(r"\n", " ", message)
    words_in_message = message.split(" ")

    random_case = random.randint(0,0)
    if random_case == 0:
        sentence_lengh = random.randint(2, 15)
        print('Длина ответа будет -- ', sentence_lengh)
        first_word_in_sentence_index = random.randrange(0, (len(words_in_message)))
        sentence = words_in_message[first_word_in_sentence_index]
        print('Первое слово ответа -- ', sentence)
        for i in range(sentence_lengh):
            print("Ща будет второе слово - ", i)
            next_word_in_sentence = select_next_word(words_in_message[first_word_in_sentence_index], chat_id)
            print("Следующее слово - ", next_word_in_sentence)
            if next_word_in_sentence == None:
                pass
            else:
                sentence.append(next_word_in_sentence)
                first_word_in_sentence = next_word_in_sentence
        generated_message = ' '.join(sentence)
        print(generated_message)
        return generated_message

    elif random_case == 1:
        pass
    elif random_case == 2:
        pass





























'''
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
