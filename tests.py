import re


message = 'Из западного ануса сосёте вы говно, за кока-колу сраную продались вы давно (точнее - в 12:45). Подстилки подпиндосные, дадим вам пососать, и знать тогда вы будете, как анус им лизать! Лижете-соёте.'

message = re.sub(r"http\S+", " ", message)
message = re.sub(r"\S*@\S*\s?", " ", message)
message = re.sub(r"^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$", " ", message)
message = re.sub(r"\n", " ", message)
message = message.replace('?!',' ?! ').replace('??',' ?? ').replace('!!',' !! ').replace('...',' ... ').replace(',', ' , ').replace('.',' . ').replace('-',' - ').replace('?',' ? ').replace('!',' ! ').replace('«',' « ').replace('»',' » ').replace(';',' ; ')
words_in_message = message.split()
print(words_in_message)