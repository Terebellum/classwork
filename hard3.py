n = list(map(int, input().split()))
m = list(map(int, input().split()))

o = []

i = 0
j = 0
while ((i < (len(n) - 1))  or (j < (len(m) - 1 ))):
    if n[i] >= m[j] and j != (len(m) - 1 ):
        o.append(m[j])
        j += 1;
    else:
        o.append(n[i])
        if i != len(n) - 1:
            i += 1;

print(o)
