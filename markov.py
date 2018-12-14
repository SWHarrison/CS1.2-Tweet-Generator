from dictogram import Dictogram, get_word_list, sample_dictionary, load_words
from sample import sample_dictionary
from circular_buffer import CircularBuffer
import random, pickle

file = open("books.txt",'r')
books = file.readlines()
file.close()
file_name = "raw_corpus_part.txt"
n = 4
text = load_words(file_name)
print(text)

markov = pickle.load( open( "save.p", "rb" ) )

for key in markov:
    print("key: " + str(key))
    print(markov[key])

sentence = ""
start_index = random.randrange(len(text)-n)
current = CircularBuffer(n)
for i in range(n):
    current.enqueue(text[start_index+i])
for i in range(8):
    key = tuple(current.items())
    new_word = sample_dictionary(markov[key])
    sentence += " " + new_word
    current.enqueue(new_word)

sentence += "."
sentence = sentence[1].upper() + sentence[2:]
book = books[random.randrange(len(books))].rstrip()
chapter = random.randrange(20)
verse = random.randrange(100)
print(book + " " + str(chapter) + ":" + str(verse) + " " + sentence)
