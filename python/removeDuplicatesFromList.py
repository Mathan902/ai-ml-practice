numbers = [1, 2, 3, 2, 4, 1, 5, 3]

res = []

for num in numbers:
    if num not in res:
        res.append(num)
print("The list after removing duplicates is:", res)