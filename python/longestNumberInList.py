numbers = [1, 23, 456, 7890, 12, 34567]

maxNo = numbers[0]

for num in numbers:
    maxNo = max(num, maxNo)
print("The longest number in the list is:", maxNo)