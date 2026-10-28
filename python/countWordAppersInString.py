sentence = "python is easy and python is powerful"

count_dict = {}

for word in sentence.split():
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1

for word, count in count_dict.items():
    print(f"The word '{word}' appears {count} times in the sentence.")