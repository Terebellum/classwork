with open("text.txt", "r", encoding='utf-8') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    maxl = 0
    output = []

    for line in lines:
        maxl = max(len(line), maxl)
        
    for i in range(2, maxl+1):
        for line in lines:
            if len(line) == i:
                print(line)
