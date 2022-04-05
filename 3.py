with open("text.txt", "r") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    maxl = 0
    output = []

    for line in lines:
        maxl = max(len(line), maxl)
        
    for line in lines:
        if len(line) == maxl:
            output.append(line)

for i in output:
    print(i)
