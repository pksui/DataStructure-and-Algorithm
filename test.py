from collections import deque

s = deque()

s.append(1)
s.pop()

if s[0] == 1:
    print("yes")
else:
    print("No")