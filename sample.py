import histogram, random, time

def sample_lists_of_lists(text, histogram_list):

    #histogram_list = histogram.histogram_list_of_lists(text)
    max = len(text)
    value = random.randrange(max)

    count = 0
    index = 0
    while(count < value):
        index += 1
        count += histogram_list[index][1]


    return histogram_list[index][0]

def sample_count_of_lists(text, histogram_list):

    #histogram_list = histogram.histogram_count_lists_try_catch(text)
    #print(histogram_list)
    max = len(text)
    value = random.randrange(max)
    #print(value)

    count = 0
    index = -1
    while(count < value):
        to_add = histogram_list[index][0] * len(histogram_list[index][1])
        count += to_add
        index += 1

    type_index = random.randrange(len(histogram_list[index][1]))

    return histogram_list[index][1][type_index]


file_name = "notes.txt"

#print(sample_lists_of_lists(file_name))
text = histogram.load_words(file_name)
histogram_list = histogram.histogram_count_lists_try_catch(text)
current = time.perf_counter()
words = list()
for i in range(1000):
    word = sample_count_of_lists(text, histogram_list)
    words.append(word)

samples = histogram.histogram_count_lists_try_catch(words)
print(samples)
print(time.perf_counter() - current)

#text = histogram.load_words(file_name)
histogram_list2 = histogram.histogram_list_of_lists(text)
current2 = time.perf_counter()
words = list()
for i in range(1000):
    word = sample_lists_of_lists(text, histogram_list2)
    words.append(word)

samples = histogram.histogram_count_lists_try_catch(words)
print(samples)
print(time.perf_counter() - current2)
