import re
message = ["#", "калговна"]
good_looking_sentence = ' '.join(message)
good_looking_sentence = re.sub(r"\s(?=[ , . ! ? : ; …])", "", good_looking_sentence)
good_looking_sentence = re.sub(r"(?<=[« \( \] \{ ])\s|\s(?=[»\) \] \} ])", "", good_looking_sentence)
good_looking_sentence = re.sub(r"(?<=[a-zA-Z])\s(?=['`’])|((?<=['`’])\s(?=[a-zA-Z]))", "", good_looking_sentence)
good_looking_sentence = re.sub(" - ", "-", good_looking_sentence)
good_looking_sentence = re.sub(" / ", "/", good_looking_sentence)
if good_looking_sentence.count('"') % 2 == 1:
        good_looking_sentence = re.sub(r'"', '', good_looking_sentence)
else:
        good_looking_sentence = re.sub(r"([\"']+[*\w\W]+[\"])", r" \1 ", good_looking_sentence)
good_looking_sentence = re.sub(r"(?<=[?!\.,@#$%^&…])[?!\.,@#$%^&*()\"';:+=-…]+", "", good_looking_sentence)
good_looking_sentence = re.sub(r"(?<=[0..9])\s(?=\%)", "", good_looking_sentence)
good_looking_sentence = re.sub(r"(?<=#)\s(?=\w)", "", good_looking_sentence)
good_looking_sentence = re.sub(r"\s\*\s", "*", good_looking_sentence)
print(message)
print(good_looking_sentence)
