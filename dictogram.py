#!python
from __future__ import division, print_function  # Python 2 and 3 compatibility
from circular_buffer import CircularBuffer
import re, random


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        self.tokens += count
        if word in self:
            self[word] += count
        else:
            self[word] = count
            self.types += 1

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        if word in self:
            return self[word]
        else: return 0


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()

def get_word_list(text, word_to_find, n):
    to_return = list()
    current_words = CircularBuffer(n)
    for i in range(0,n-1):
        current_words.enqueue(text[i].lower())
    index = 0
    for i in range(0,len(text)-n+1):
        current_words.enqueue(text[i].lower())
        compare = tuple(current_words.items())
        if(compare == word_to_find):
            to_return.append(text[index+1])
        index += 1

    return to_return

def load_words(file_name):
    '''Loads words from a file and cleans text of most special characters'''
    file = open(file_name,'r')
    read_words = file.readlines()
    file.close()
    pattern = '\d*\d*\d:\d*\d*\d'
    no_num = list()
    for line in read_words:
        no_num.append((re.sub(pattern, "" , line)))
    words = list()
    for line in no_num:
        split_line = line.strip().split(" ")
        for word in split_line:
            if(word.lower() != ""):
                words.append(word.strip(":;(),!.1234567890").lower())

    return words

def sample_dictionary(histogram_dict):
    #Great solution but Zurich laughed at it
    #histogram_list = list(histogram_dict.items())
    #return sample_lists_of_lists(text_length,histogram_list)
    max = 0
    for key in histogram_dict:
        max += histogram_dict[key]
    value = random.randrange(max)

    count = 0
    for key in histogram_dict:
        count += histogram_dict[key]
        if(count > value):
            return key


def main():

    file = open("books.txt",'r')
    books = file.readlines()
    file.close()
    file_name = "raw_corpus_part.txt"
    n = 2
    sentence = list()
    text = load_words(file_name)
    current_words = CircularBuffer(n)
    for i in range(n-1):
        current_words.enqueue(text[i].lower())
    new_text = text[n-1:]
    markov = {}
    for word in new_text:

        current_words.enqueue(word.lower())
        key = tuple(current_words.items())
        if key not in markov:
            words = get_word_list(text, key, n)
            markov[key] = Dictogram(words)

    #for key in markov:
    #    print("key: " + str(key))
    #    print(markov[key])


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
    book = books[random.randrange(len(books))].rstrip()
    chapter = random.randrange(20)
    verse = random.randrange(100)
    print(book + " " + str(chapter) + ":" + str(verse) + " " + sentence)



if __name__ == '__main__':
    main()
