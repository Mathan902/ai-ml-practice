sentence = "python is easy and python is powerful"

count_dict = {}

max_count = None

for word in sentence.split():
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1

    if max_count is not None:
        if count_dict[word] > count_dict[max_count]:
            max_count = word
    else:
        max_count = word

print(f"The most frequent word is '{max_count}' with a count of {count_dict[max_count]}.")