from dictogram import Dictogram, get_word_list, sample_dictionary, load_words
from sample import sample_dictionary
from circular_buffer import CircularBuffer
import random, pickle

#Using Thomas Lee's framework
class Markov_nth_order(dict):
    def __init__(self, order, word_list=None):
        super(Markov_nth_order, self).__init__() # Initialise empty dictionary
        self.types = 0
        self.tokens = 0
        self.order = order
        if word_list is not None:
            self.create_dict_of_dict(word_list)

    def create_dict_of_dict(self, text):
        """
        Creating a dictionary of {(current_tuple):{next_type: 1}} structure.
        """
        current_words = CircularBuffer(self.order)
        for i in range(self.order-1):
            current_words.enqueue(text[i].lower())
        new_text = text[self.order-1:]
        for i in range(len(new_text)-self.order):

            current_words.enqueue(new_text[i].lower())
            key = tuple(current_words.items())
            if key not in self:
                self[key] = Dictogram()

            self[key].add_count(new_text[i+1],1)

    def generate_random_sentence(self, text, sentence_length=12):
        """
        Generating a random sentence from given corpus using markov chains,
        returning as a list.
        """
        sentence = ""
        start_index = random.randrange(len(text)-self.order)
        current = CircularBuffer(self.order)
        for i in range(self.order):
            current.enqueue(text[start_index+i])
        for i in range(sentence_length):
            key = tuple(current.items())
            new_word = sample_dictionary(self[key])
            sentence += " " + new_word
            current.enqueue(new_word)

        sentence += "."
        return sentence

if __name__ == '__main__':
    file_name = "raw_corpus_part.txt"
    text = load_words(file_name)
    markov = Markov_nth_order(4,text)
    print(markov.generate_random_sentence(text))
