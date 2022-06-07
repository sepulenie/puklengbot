from asyncio import SendfileNotAvailableError
import sqlite3, random, re
from xml.sax.saxutils import prepare_input_source

conn = sqlite3.connect("dickdump.db", check_same_thread=False)
cursor = conn.cursor()

def add_words_in_message_to_dictionary(message, chat_id):
    message = re.sub(r"http\S+", " ", message)
    message = re.sub(r"\S*@\S*\s?", " ", message)
    message = re.sub(r"^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$", " ", message)
    message = re.sub(r"\n", " ", message)
    message = message.replace('?!',' ?! ').replace('??',' ?? ').replace('!!',' !! ').replace('...',' ... ').replace(',', ' , ').replace('.',' . ').replace('-',' - ').replace('?',' ? ').replace('!',' ! ').replace('«',' « ').replace('»',' » ').replace(';',' ; ')
    words_in_message = message.split()
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
                search_result_word_1.update({word_1: (search_result_word_1.get(word_1)+10)})
                cursor.execute("UPDATE dickdump SET word_1=? WHERE word_0=?", (repr(search_result_word_1), search_result_word_0))
            else:
                search_result_word_1.update({word_1:1})
                cursor.execute("UPDATE dickdump SET word_1=? WHERE word_0=?", (repr(search_result_word_1), search_result_word_0))
    conn.commit()







def generate_message(message, chat_id):
    message = re.sub(r"http\S+", " ", message)
    message = re.sub(r"\S*@\S*\s?", " ", message)
    message = re.sub(r"^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$", " ", message)
    message = re.sub(r"\n", " ", message)
    message = message.replace('?!',' ?! ').replace('??',' ?? ').replace('!!',' !! ').replace('...',' ... ').replace(',', ' , ').replace('.',' . ').replace('-',' - ').replace('?',' ? ').replace('!',' ! ').replace('«',' « ').replace('»',' » ').replace(';',' ; ')
    words_in_message = message.split()                                           #разделяем сообщение на слова
    #print('Начинаем генерировать ответ на ', words_in_message)
    random_case = random.randint(0,0)                                               #выбор случайного типа фразы
    if random_case == 0:                                                            #Просто случайный набор слов
        sentence_lengh = random.randint(10, 50)                                      #длина ответа будет от и до
        #print('Длина ответа случайная и будет составлять -- ', sentence_lengh)
        current_word_in_sentence = words_in_message[random.randrange(0, (len(words_in_message)))] #первое слово ответа это случайное слово входного сообщения
        #print("Первое слово это ", current_word_in_sentence, "---ТИП---: ", type(current_word_in_sentence))
        sentence = [current_word_in_sentence]                                       #фраза пока что состоит только из первого слова
        #print('Фраза пока что выглядит вот так -- ', sentence, "---ТИП---: ", type(sentence))                                  
        for i in range(sentence_lengh):                                                          #начало
            #print("Выбор следующего слова, попытка №", i)
            search = "SELECT word_1 FROM dickdump WHERE chat_id=? AND word_0=?"     #есть ли первое слово в базе
            cursor.execute(search, [(chat_id), (current_word_in_sentence)])         #
            search_result = cursor.fetchone()
            if search_result == None:
                final_sentence = ' '.join(sentence)
                final_sentence = final_sentence.replace(" ,", ", ").replace(" .",". ").replace(" -","-").replace(" ?","? ").replace(" !","! ").replace(" «","«").replace(" »","»").replace(" ;","; ").replace("  "," ").replace(" :", ": ")
                return final_sentence
            else:
                search_result_as_dict = eval(search_result[0])
                #print("Второе слово будет выбрано из этих -- ")
                keys_list = list(search_result_as_dict.keys())
                #print("Список слов - ", keys_list)
                values_list = list(search_result_as_dict.values())
                #print("Список их весов - ", values_list)
                random_next_word = random.choices(keys_list, values_list, k=1)
                #print("Следующее случайное слово -- ", random_next_word[0], "---ТИП---: ", type(random_next_word[0]))
                sentence.append(random_next_word[0])
                current_word_in_sentence = random_next_word[0]
                #print("Теперь следующее случайное слово -- ", current_word_in_sentence, "---ТИП---: ", type(current_word_in_sentence))

        final_sentence = ' '.join(sentence)
        final_sentence = final_sentence.replace(" ,", ", ").replace(" .",". ").replace(" -","-").replace(" ?","? ").replace(" !","! ").replace(" «","«").replace(" »","»").replace(" ;","; ").replace("  "," ")
        #print("В общем ответ пока что выглядит так -- ", final_sentence)
        return final_sentence


    elif random_case == 1:
        sentence_lengh = random.randint(1, 5)                                      
        current_word_in_sentence = words_in_message[random.randrange(0, (len(words_in_message)))]
        sentence = [current_word_in_sentence]
        random_next_word = ''
        for i in range(sentence_lengh):
            while random_next_word[0] != '.' or random_next_word[0] != '!' or random_next_word[0] != '?':
                search = "SELECT word_1 FROM dickdump WHERE chat_id=? AND word_0=?"     
                cursor.execute(search, [(chat_id), (current_word_in_sentence)])         
                search_result = cursor.fetchone()
                if search_result == None:
                    sentence.append['.']
                    final_sentence = ' '.join(sentence)
                    final_sentence = final_sentence.replace(" ,", ", ").replace(" .",". ").replace(" -","-").replace(" ?","? ").replace(" !","! ").replace(" «","«").replace(" »","»").replace(" ;","; ").replace("  "," ").replace(" :", ": ")
                    return final_sentence
                else:
                    search_result_as_dict = eval(search_result[0])
                    keys_list = list(search_result_as_dict.keys())
                    values_list = list(search_result_as_dict.values())
                    random_next_word = random.choices(keys_list, values_list, k=1)  
                    sentence.append(random_next_word[0])
                    current_word_in_sentence = random_next_word[0]
        final_sentence = ' '.join(sentence)
        final_sentence = final_sentence.replace(" ,", ", ").replace(" .",". ").replace(" -","-").replace(" ?","? ").replace(" !","! ").replace(" «","«").replace(" »","»").replace(" ;","; ").replace("  "," ")
        print("В общем ответ пока что выглядит так -- ", final_sentence)
        return final_sentence



            
            
            
            
            
        









'''next_word_in_sentence = select_next_word(first_word_in_sentence, chat_id)
            print("Следующее слово - ", next_word_in_sentence)












            
            if next_word_in_sentence == None:
                pass
            else:
                sentence.append(next_word_in_sentence)
                first_word_in_sentence = next_word_in_sentence
        generated_message = ' '.join(sentence)
        print(generated_message)
        return generated_message

    
    elif random_case == 2:
        pass
'''




























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
