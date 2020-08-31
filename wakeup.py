word_dict = {}
def autism():
    data = 'одна рыба две рыбы три рыбы четыре рыбы пять рыб блядь сколько можно считать рыб один один два три четыре'
    

    ind_words = data.split()
    print(ind_words)

    def make_pairs(ind_words):
        for i in range(len(ind_words) - 1):
            yield (ind_words[i], ind_words[i + 1])
    pair = make_pairs(ind_words)



    for word_1, word_2 in pair:
       if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
       else:
            word_dict[word_1] = [word_2]


autism()
print(word_dict)