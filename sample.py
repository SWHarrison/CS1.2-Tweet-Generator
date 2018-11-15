import histogram, random, time

def sample_lists_of_lists(text_length, histogram_list):
    '''Takes a histogram of and returns a random word based on weights.
    Uses a list of list approach'''
    max = text_length
    value = random.randrange(max)

    #Counts number of occurences of each token, and when the value
    #of the cumulative tokens is greater than the random value it
    #returns that index.
    count = 0
    index = -1
    while(count < value):
        index += 1
        count += histogram_list[index][1]


    return histogram_list[index][0]


def sample_dictionary(text_length, histogram_dict):
    histogram_list = list(histogram_dict.items())
    return sample_lists_of_lists(text_length,histogram_list)


def sample_count_of_lists(text_length, histogram_list):
    '''Takes a histogram of and returns a random word based on weights.
    Uses a count of lists approach'''
    max = text_length
    value = random.randrange(max)

    #Counts number of occurences of each token, and when the value
    #of the cumulative tokens is greater than the random value it
    #returns a random token in the array of words with the index
    #number of occurences.
    count = 0
    index = -1
    while(count < value):
        to_add = histogram_list[index+1][0] * len(histogram_list[index+1][1])
        count += to_add
        index += 1

    type_index = random.randrange(len(histogram_list[index][1]))

    return histogram_list[index][1][type_index]

if __name__ == "__main__":
    file_name = "notes.txt"

    #print(sample_lists_of_lists(file_name))
    text = histogram.load_words(file_name)
    text_length = len(text)
    histogram_list = histogram.histogram_count_lists_try_catch(text)
    #print(histogram_list)
    current = time.time()
    words = list()
    for i in range(10000):
        word = sample_count_of_lists(text_length, histogram_list)
        words.append(word)

    print(time.time() - current)

    samples = histogram.histogram_count_lists_try_catch(words)
    print(samples)

    #text = histogram.load_words(file_name)
    '''histogram_list2 = histogram.histogram_dictionary(text)
    current2 = time.time()
    words = list()
    for i in range(10000):
        word = sample_dictionary(text_length, histogram_list2)
        words.append(word)'''

    histogram_list2 = histogram.histogram_list_of_lists(text)
    current2 = time.time()
    words = list()
    for i in range(10000):
        word = sample_lists_of_lists(text_length, histogram_list2)
        words.append(word)

    print(time.time() - current2)

    samples = histogram.histogram_count_lists_try_catch(words)
    print(samples)
