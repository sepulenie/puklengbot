
import sqlite3, random, re

conn = sqlite3.connect("dickdump.db", check_same_thread=False)
cursor = conn.cursor()

def add_words_in_message_to_dictionary(message, chat_id):
    message = re.sub(r"http\S+", " ", message)
    message = re.sub(r"\S*@\S*\s?", " ", message)
    message = re.sub(r"^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$", " ", message)
    message = re.sub(r"\n", " ", message)
    words_in_message = re.findall(r"[\w]+|[^\s\w]", message)  
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
                search_result_word_1.update({word_1: (search_result_word_1.get(word_1)+5)})
                cursor.execute("UPDATE dickdump SET word_1=? WHERE word_0=?", (repr(search_result_word_1), search_result_word_0))
            else:
                search_result_word_1.update({word_1:1})
                cursor.execute("UPDATE dickdump SET word_1=? WHERE word_0=?", (repr(search_result_word_1), search_result_word_0))
    conn.commit()


def first_word_finder(words_in_message):
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


def generate_message(message, chat_id):
    message = re.sub(r"http\S+", " ", message)
    message = re.sub(r"\S*@\S*\s?", " ", message)
    message = re.sub(r"^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$", " ", message)
    message = re.sub(r"\n", " ", message)
    words_in_message = re.findall(r"[\w]+|[^\s\w]", message)                                          
    random_case = 1  
    if random_case == 0:                                                            
        sentence_lengh = random.randint(10, 500)                                      
        current_word_in_sentence = words_in_message[random.randrange(0, (len(words_in_message)))]
        sentence = [current_word_in_sentence]              
        for i in range(sentence_lengh):
            search = "SELECT word_1 FROM dickdump WHERE chat_id=? AND word_0=?"
            cursor.execute(search, [(chat_id), (current_word_in_sentence)])
            search_result = cursor.fetchone()
            if search_result == None:
                final_sentence = ' '.join(sentence)
                final_sentence = final_sentence.replace(" ,", ", ").replace(" .",". ").replace(" -","-").replace(" ?","? ").replace(" !","! ").replace(" «","«").replace(" »","»").replace(" ;","; ").replace("  "," ").replace(" :", ": ")
                return final_sentence
            else:
                search_result_as_dict = eval(search_result[0])
                keys_list = list(search_result_as_dict.keys())
                values_list = list(search_result_as_dict.values())
                random_next_word = random.choices(keys_list, weights=values_list, k=1)
                sentence.append(random_next_word[0])
                current_word_in_sentence = random_next_word[0]
        final_sentence = ' '.join(sentence)
        final_sentence = final_sentence.replace(" ,", ", ").replace(" .",". ").replace(" -","-").replace(" ?","? ").replace(" !","! ").replace(" «","«").replace(" »","»").replace(" ;","; ").replace("  "," ")
        return final_sentence
    elif random_case == 1:
        max_sentences_amount = random.randint(2, 6)
        sentences_amount = 0
        current_word_in_sentence = first_word_finder(words_in_message)
        sentence = [current_word_in_sentence]
        while sentences_amount < max_sentences_amount:
            max_sentence_lengh = random.randint(2, 14)
            sentence_lengh = 0
            sentences_amount += 1
            while sentence_lengh < max_sentence_lengh:
                sentence_lengh += 1
                search = "SELECT word_1 FROM dickdump WHERE chat_id=? AND word_0=?"
                cursor.execute(search, [(chat_id), (current_word_in_sentence)])
                search_result = cursor.fetchone()
                if search_result == None:
                    final_sentence = ' '.join(sentence)
                    final_sentence = final_sentence+"."
                    final_sentence = final_sentence.replace(" ,", ", ").replace(" .",". ").replace(" -","-").replace(" ?","? ").replace(" !","! ").replace(" «","«").replace(" »","»").replace(" ;","; ").replace("  "," ").replace(" :", ": ")
                    return final_sentence   
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
        final_sentence = ' '.join(sentence)
        final_sentence = final_sentence.replace(" ,", ", ").replace(" .",". ").replace(" -","-").replace(" ?","? ").replace(" !","! ").replace(" «","«").replace(" »","»").replace(" ;","; ").replace("  "," ").replace(" :", ": ")
        return final_sentence