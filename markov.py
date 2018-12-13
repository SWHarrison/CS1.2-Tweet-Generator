import dictogram
from sample import sample_dictionary
from circular_buffer import CircularBuffer
import random

file = open("books.txt",'r')
books = file.readlines()
file.close()
file_name = "raw_corpus_part.txt"
n = 3
text = dictogram.load_words(file_name)
file_name = "notes.txt"
text2 = dictogram.load_words(file_name)
text += text2

sentence = ""
start_index = random.randrange(len(text)-n)
current = CircularBuffer(n)
for i in range(n):
    current.enqueue(text[start_index+i])

sentence_length = random.randint(8,20)
for i in range(sentence_length):
    key = tuple(current.items())
    word_list = dictogram.get_word_list(text, key, n)
    dicto = dictogram.Dictogram(word_list)
    new_word = sample_dictionary(dicto)
    sentence += " " + new_word
    current.enqueue(new_word)

sentence += "."
sentence = sentence[1].upper() + sentence[2:]
book = books[random.randrange(len(books))].rstrip()
chapter = random.randrange(20)
verse = random.randrange(100)
print(book + " " + str(chapter) + ":" + str(verse) + " " + sentence)
