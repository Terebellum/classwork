with open("text.txt", "r", encoding='utf-8') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    for line in lines:
        pi = None
        for i in line:
            if pi == i:
                print(line)
            pi = i
