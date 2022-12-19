import random
from collections import defaultdict
word_pairs = defaultdict(int)



def process_message(message):
  # Split the message into a list of words
  words = message.split()
  
  # Initialize a defaultdict to store the word pairs and their frequency

  # Iterate through the words and add each pair to the defaultdict
  for i in range(len(words) - 1):
    word_pairs[(words[i], words[i + 1])] += 1
  
  return word_pairs

def generate_random_message(word_pairs):
  # Choose a random word pair from the word_pairs defaultdict
  word_pair = random.choice(list(word_pairs.keys()))
  
  # Concatenate the words in the pair and return the result
  return " ".join(word_pair)


print(process_message("одна рыба, две рыбы, три рыбы, четыре рыбы. Пять рыб. Двадцать одна рыба, тридцать четыре рыбы. одна клешня, две клешни"))
generate_random_message(word_pairs)