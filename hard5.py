s = input()
ss = input()

N = len(ss)

answer = None

for i in range(len(s)):
    if s[i:i+N] == ss:
        answer = i

if answer == None:
    print("No answer")
else:
    print(answer)
