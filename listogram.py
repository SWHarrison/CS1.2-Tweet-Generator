#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
import time, random
from queue import Queue

class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        for item in self:
            if item[0] == word.lower():
                item[1] += count
                self.tokens += 1
                return

        self.types += 1
        self.tokens += 1
        to_add = list()
        to_add.append(word.lower())
        to_add.append(count)
        self.append(to_add)



    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        for item in self:
            if(item[0] == word.lower()):
                return item[1]

        return 0

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        # TODO: Check if word is in this histogram
        for item in self:
            if(item[0] == word.lower()):
                return True

        return False

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # TODO: Implement linear search to find index of entry with target word
        index = 0
        for item in self:
            if(item[0] == target.lower()):
                return index

        return None

    def sample_lists_of_lists(self):
        '''Takes a histogram of and returns a random word based on weights.
        Uses a list of list approach'''
        max = self.tokens
        value = random.randrange(max)

        #Counts number of occurences of each token, and when the value
        #of the cumulative tokens is greater than the random value it
        #returns that index.
        count = 0
        index = -1
        while(count < value):
            index += 1
            count += self[index][1]


        return self[index][0]

def print_histogram(word_list):
    #print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def get_word_list(text, words_to_find):
    to_return = list()
    index = 0
    for word in text:
        if(word.lower() == word_to_find):
            if(index < len(text)-1):
                to_return.append(text[index+1])
        index += 1

    return to_return


def load_words(file_name):
    '''Loads words from a file and cleans text of most special characters'''
    file = open(file_name,'r')
    read_words = file.readlines()
    file.close()
    words = list()
    for line in read_words:
        split_line = line.strip().split(" ")
        for word in split_line:
            if(word.lower() != ""):
                words.append(word.strip("(),!."))

    return words


def main():
    '''import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())'''

    sentence_length = 8
    file_name = "notes.txt"
    sentence = list()
    text = load_words(file_name)
    new_word = text[random.randrange(len(text))]
    new_text = text

    for i in range(sentence_length):
        words_list = get_word_list(new_text, new_word)
        if(len(words_list) > 0):
            textogram = Listogram(words_list)
            new_word = textogram.sample_lists_of_lists()
            sentence.append(new_word)
        else:
            print(new_word)

    print(sentence)



if __name__ == '__main__':
    main()
