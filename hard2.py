def is_sorted(arr):
    increased = True
    decreased = True
    for i in range(len(arr)- 1):
        if arr[i] < arr[i+1]:
            decreased = False
        if arr[i] > arr[i+1]:
            increased = False
    return increased or decreased
    


n = list(map(int, input().split()))

print(is_sorted(n)) 
