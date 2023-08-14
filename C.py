from collections import deque

def rotate_list(target): 
    rotate_deque = deque(target)
    rotate_deque.rotate(1)
    return rotate_deque

N,M = map(int, input().split())
S = input()
s = [char for char in S]
c = list(map(int, input().split()))
color_chars = [deque() for _ in range(M)]
for i in range(N):
    color_chars[c[i]-1].append(s[i])

for i in range(M):
    color_chars[i] = rotate_list(color_chars[i])

for i in range(N):
    ans = color_chars[c[i]-1].popleft()
    print(ans, end="")