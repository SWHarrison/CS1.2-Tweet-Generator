from n_order_markov import Markov_nth_order

def main():
    text = load_words("raw_corpus_part.txt")
    markov = Markov_nth_order(4, text)

    markov.create_dict_of_dict(word_list)
    sentence_list = markov.generate_random_sentence(word_list, 20)
    # print(" ".join(sentence_list))
    sentence_list = " ".join(sentence_list)

    # random_word_weighted_dict = random_word_histogram(sentence_list,histogram_dict)
    # print(random_word_weighted_dict)
    return sentence_list

if __name__ == '__main__':
    print(main())
