n = [3, 6, -3, 1, 5, -9, 3, 6, 7, -8]

summ = 0
count = 0
for i in n:
    if i > 0:
        summ += i
    if i < 0:
        count += 1
print(summ, count)
