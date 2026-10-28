numbers = [1, 23, 456, 7890, 12, 34567]

n1 = numbers[0]
n2 = n1

for index, num in enumerate(numbers,1):
    if num > n1:
        n2 = n1
        n1 = num
    elif num > n2 and num != n1:
        n2 = num
print("The second largest number in the list is:", n2)