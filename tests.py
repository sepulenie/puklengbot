import re
sentence = ['Хуй', "Пизда.", "\n", ",", "\n","Собака"]

good_looking_sentence = ' '.join(sentence)
print(good_looking_sentence)
good_looking_sentence = re.sub(r"[\t](?=[ , . ! ? : ; …])", "", good_looking_sentence)

print(good_looking_sentence)