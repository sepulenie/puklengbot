import re, random


message = 'из западного ануса сосёте вы говно, за кока-колу Сраную продались вы давно ((Точнее - в 12:45). подстилки подпиндосные, дадим вам пососать! И знать тогда вы будете, как анус им лизать!! лижете-сосёте.'

message = re.sub(r"http\S+", " ", message)
message = re.sub(r"\S*@\S*\s?", " ", message)
message = re.sub(r"^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$", " ", message)
message = re.sub(r"\n", " ", message)
message = re.sub(r'([!@#%\^&\*\(\):;"\',\./\\]+)', r' \1 ', message)
words_in_message = message.split()
print(words_in_message)
