n = []

while(True):
    a = float(input())
    if a == 0:
        break
    n.append(a)

maxe = max(n)
print(maxe)

count = 0

for i in n:
    if maxe == i:
        count += 1

print(count)
        
