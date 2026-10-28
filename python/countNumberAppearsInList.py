numbers = [1, 2, 3, 2, 4, 1, 2, 5, 3, 2]

count_dict = {}

for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

for num, count in count_dict.items():
    print(f"The number {num} appears {count} times in the list.")