'''
ver. 0.4.2


'''
import sqlite3, random, re

conn = sqlite3.connect("dickdump.db", check_same_thread=False)
cursor = conn.cursor()
zachem = ('зачем', 'зачем?', 'а зачем?', 'а зачем', 'но зачем', 'но зачем?', 'да зачем', 'да зачем?', 'ну зачем', 'ну зачем?', 'zachem', 'зчем','зачм','зчм')
beestickers = ['CAACAgIAAxkBAAEV9dViz62AYAzSdU9JCqf2ooWmW5QZWwAC-QEAAjHTyQGcZWU2FhByTSkE', 'CAACAgIAAxkBAAEV9eliz7EBrEgPKMrNOi0ZJqZustMp8AACdRIAAuQBqEjwo2HdYWpBnikE']

    
def make_text_look_good(sentence = list):
    good_looking_sentence = ' '.join(sentence)
    good_looking_sentence = re.sub(r"\s(?=[ , . ! ? : ; …])", "", good_looking_sentence)
    good_looking_sentence = re.sub(r"(?<=[«\(\[\{“])\s|\s(?=[»\)\]\}”])", "", good_looking_sentence)
    good_looking_sentence = re.sub(r"(?<=[a-zA-Z])\s(?=['`’])|((?<=['`’])\s(?=[a-zA-Z]))", "", good_looking_sentence)
    good_looking_sentence = re.sub(r"(?<=[❗⚡])\s", "", good_looking_sentence)
    good_looking_sentence = re.sub(" - ", "-", good_looking_sentence)
    good_looking_sentence = re.sub(" / ", "/", good_looking_sentence)
    if good_looking_sentence.count('"') % 2 == 1:
        good_looking_sentence = re.sub(r'"', '', good_looking_sentence)
    good_looking_sentence = re.sub(r"\"\s*([^\"]*?)\s*\"", "\1", good_looking_sentence)
    return good_looking_sentence



def make_greentext_look_good(sentence = list):
    good_looking_greentext = ' '.join(sentence)
    good_looking_greentext = re.sub(r"(?<=>)\s", "", good_looking_greentext)
    good_looking_greentext = re.sub(r"\s(?=>)", "", good_looking_greentext)
    good_looking_greentext = re.sub(r"\s(?=[ , . ! ? : ; …])", "", good_looking_greentext)
    good_looking_greentext = re.sub(" - ", "-", good_looking_greentext)
    return good_looking_greentext



def add_words_in_message_to_dictionary(message, chat_id):
    message = re.sub(r"http\S+", " ", message)
    message = re.sub(r"\S*@\S*\s?", " ", message)
    message = re.sub(r"\.\.\.", "…", message)
    message = re.sub(r"(?<=[\s\w])\n+", ". ", message)
    message = re.sub(r"(?<=[^\s\w])[^\s\w]", " ", message)
    message = re.sub(r">"," ", message)
    message = re.sub(r"\n", " ", message)
    message = re.sub(" - ", ' — ',message)
    if message[-1].isalpha() == True:
        message = message+"."
    else:
        pass
    if message[0].isalpha() == True:
        message = message[0].upper()+message[1:]
    else:
        pass
    message = re.sub(r"\.\.\.", "…", message)
    words_in_message = re.findall(r"\d+\%|\w+[-'\.\*]+\w+|[\w#]+|[^\s\w]", message)
    try:
        def make_pairs(words_in_message):
            for i in range(len(words_in_message)- 1):
                yield (words_in_message[i], words_in_message[i + 1])
        pair_of_words = make_pairs(words_in_message)
        for word_0, word_1 in pair_of_words:
            search = "SELECT * FROM dickdump WHERE chat_id=? AND word_0=?"
            cursor.execute(search, [(chat_id), (word_0)])
            search_result = (cursor.fetchone())
            if search_result == None:
                cursor.execute("INSERT INTO dickdump VALUES (?,?,?,?)", (chat_id, word_0, repr({word_1: 1}), 0))
            else:
                search_result_word_0 = search_result[1]
                search_result_word_1 = dict
                search_result_word_1 = eval(search_result[2])
                if word_1 in search_result_word_1.keys():
                    search_result_word_1.update({word_1: (search_result_word_1.get(word_1)+len(word_1))})
                    cursor.execute("UPDATE dickdump SET word_1=? WHERE word_0=? AND chat_id=?", (repr(search_result_word_1), search_result_word_0, chat_id))
                else:
                    search_result_word_1.update({word_1:1})
                    cursor.execute("UPDATE dickdump SET word_1=? WHERE word_0=? AND chat_id=?", (repr(search_result_word_1), search_result_word_0, chat_id))
        cursor.execute("UPDATE dickdump SET is_first=? WHERE word_0=? AND chat_id=?", (1, words_in_message[0], chat_id))    
        conn.commit()
    except IndexError:
        pass


def first_word_finder(words_in_message, chat_id):
    first_word_in_sentence = ''
    first_word_is_found = False
    words_in_message = words_in_message
    if len(words_in_message) == 1:
        first_word_in_sentence = words_in_message[0]
        return first_word_in_sentence
    else:
        while first_word_is_found == False and len(words_in_message) > 1:
            first_word_in_sentence = words_in_message[random.randrange(0, (len(words_in_message)))]
            if first_word_in_sentence.isalpha() == False:
                words_in_message.remove(first_word_in_sentence)
            else:
                if first_word_in_sentence[0].isupper() == False:
                    words_in_message.remove(first_word_in_sentence)
                else:
                    first_word_is_found = True
        return first_word_in_sentence

def random_first_word_finder(words_in_message, chat_id):
    first_word_in_sentence = 'Я'
    search_result = (111,'я',"\{'не':2\}")
    while search_result[1][0].isupper() == False:
        search = "SELECT * FROM dickdump WHERE chat_id=? AND is_first=1 ORDER BY random()"
        cursor.execute(search, [chat_id])
        search_result = (cursor.fetchone())
    first_word_in_sentence = search_result[1]
    return first_word_in_sentence

def generate_message(message, chat_id):
    message = re.sub(r"http\S+", " ", message)
    message = re.sub(r"\S*@\S*\s?", " ", message)
    message = re.sub(r"\W+", " ", message)
    message = re.sub(r"\n", " ", message)
    words_in_message = re.findall(r"[\w]+|[^\s\w]", message)
    max_sentences_amount = random.randint(1, 5)
    funcs = [first_word_finder, random_first_word_finder]
    #funcs1 = [random_news_emoji]
    sentences_amount = 0
    current_word_in_sentence = random.choice(funcs)(words_in_message, chat_id)
    #current_word_in_sentence = random_news_emoji_2(words_in_message, chat_id)
    sentence = [current_word_in_sentence]
    while sentences_amount < max_sentences_amount:
        max_sentence_lengh = random.randint(2, 8)
        sentence_lengh = 0
        sentences_amount += 1
        while sentence_lengh < max_sentence_lengh:
            sentence_lengh += 1
            search = "SELECT word_1 FROM dickdump WHERE chat_id=? AND word_0=?"
            cursor.execute(search, [(chat_id), (current_word_in_sentence)])
            search_result = cursor.fetchone()
            if search_result == None:
                if current_word_in_sentence.isalpha() == False:
                    break
                else:
                    current_word_in_sentence = random.choice([".", ",", "!", "?"])
                    sentence.append(current_word_in_sentence)
                break
            else:
                search_result_as_dict = eval(search_result[0])
                keys_list = list(search_result_as_dict.keys())
                values_list = list(search_result_as_dict.values())
                random_next_word = random.choices(keys_list, weights=values_list, k=1)
                if random_next_word[0] == '.' or random_next_word[0] == '?' or random_next_word[0] == '!':
                    sentence.append(random_next_word[0])
                    current_word_in_sentence = random_next_word[0]
                    break
                else:
                    sentence.append(random_next_word[0])
                    current_word_in_sentence = random_next_word[0]
    final_sentence = make_text_look_good(sentence)
    return final_sentence


def generate_news(message, chat_id):
    message = re.sub(r"http\S+", " ", message)
    message = re.sub(r"\S*@\S*\s?", " ", message)
    message = re.sub(r"\W+", " ", message)
    message = re.sub(r"\n", " ", message)
    max_sentences_amount = random.randint(1, 8)
    sentences_amount = 0
    current_word_in_sentence = random.choice(["❗", "⚡", "📍"])
    sentence = [current_word_in_sentence]
    while sentences_amount < max_sentences_amount:
        max_sentence_lengh = random.randint(4, 14)
        sentence_lengh = 0
        sentences_amount += 1
        while sentence_lengh < max_sentence_lengh:
            sentence_lengh += 1
            search = "SELECT word_1 FROM dickdump WHERE chat_id=? AND word_0=?"
            cursor.execute(search, [(chat_id), (current_word_in_sentence)])
            search_result = cursor.fetchone()
            if search_result == None:
                if current_word_in_sentence.isalpha() == False:
                    break
                else:
                    current_word_in_sentence = random.choice([".", ",", "!", "?"])
                    sentence.append(current_word_in_sentence)
                break
            else:
                search_result_as_dict = eval(search_result[0])
                keys_list = list(search_result_as_dict.keys())
                values_list = list(search_result_as_dict.values())
                random_next_word = random.choices(keys_list, weights=values_list, k=1)
                if random_next_word[0] == '.' or random_next_word[0] == '?' or random_next_word[0] == '!':
                    sentence.append(random_next_word[0])
                    current_word_in_sentence = random_next_word[0]
                    break
                else:
                    sentence.append(random_next_word[0])
                    current_word_in_sentence = random_next_word[0]
    final_sentence = make_text_look_good(sentence)
    return final_sentence



'''
if message[0] == '>' :
        firstline_len = random.randint(1,10)                                           
        max_greentext_lines = random.randint(1,4)
        greentext_lines = 0
        current_word_in_greentext = first_word_finder(words_in_message)
        greentext = ['>',current_word_in_greentext]
        max_len_of_line = 5
        while len(greentext) < firstline_len:
            search = "SELECT word_1 FROM dickdump WHERE chat_id=? AND word_0=?"
            cursor.execute(search, [(chat_id), (current_word_in_greentext)])
            search_result = cursor.fetchone()
            if search_result == None:
                if current_word_in_greentext.isalpha() == False:
                    break
                else:
                    current_word_in_greentext = first_word_finder(words_in_message)
                    greentext.append(current_word_in_greentext)
                break
            else:
                search_result_as_dict = eval(search_result[0])
                keys_list = list(search_result_as_dict.keys())
                values_list = list(search_result_as_dict.values())
                random_next_word = random.choices(keys_list, weights=values_list, k=1)
                if random_next_word[0] == '.' or random_next_word[0] == '?' or random_next_word[0] == '!':
                    greentext.append('\n')
                    current_word_in_greentext = random_next_word[0]
                    break
                else:
                    greentext.append(random_next_word[0])
                    current_word_in_greentext = random_next_word[0]
        while greentext_lines < max_greentext_lines:
            greentext_lines += 1
            greentext.append('\n')
            greentext.append('>')
            max_len_of_line = random.randint(1,10)
            currentline_len = 0
            while currentline_len < max_len_of_line:
                currentline_len += 1
                search = "SELECT word_1 FROM dickdump WHERE chat_id=? AND word_0=?"
                cursor.execute(search, [(chat_id), (current_word_in_greentext)])
                search_result = cursor.fetchone()
                if search_result == None:
                    if current_word_in_greentext.isalpha() == False:
                        current_word_in_greentext = first_word_finder(words_in_message)
                        break
                    else:
                        current_word_in_greentext = random.choice([".", ",", "!", "?"])
                        greentext.append(current_word_in_greentext)
                else:
                    search_result_as_dict = eval(search_result[0])
                    keys_list = list(search_result_as_dict.keys())
                    values_list = list(search_result_as_dict.values())
                    random_next_word = random.choices(keys_list, weights=values_list, k=1)
                    if random_next_word[0] == '.' or random_next_word[0] == '?' or random_next_word[0] == '!':
                        greentext.append('\n')
                        current_word_in_sentence = random_next_word[0]
                        break
                    else:
                        greentext.append(random_next_word[0])
                        current_word_in_sentence = random_next_word[0]
            pass



        final_greentext = make_greentext_look_good(greentext)
        return final_greentext
'''