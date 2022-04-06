arr = list(map(int, input().split()))

i = 0
N = len(arr)

while i < N - 1:
    m = i
    j = i + 1
    
    while j < N:
        if arr[j] < arr[m]:
            m = j
        j += 1

    arr[i], arr[m] = arr[m], arr[i]
    
    i += 1

print(arr)
