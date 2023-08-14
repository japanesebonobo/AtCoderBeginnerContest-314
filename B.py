N = int(input())
C = []
A = []

for _ in range(N):
    c = int(input())
    C.append(c)
    A.append(list(map(int, input().split())))

X = int(input())

ans = dict()

for i in range(N):
    for j in range(len(A[i])):
        if A[i][j] == X:
            ans[i+1] = len(A[i])

if len(ans) != 0:
# 最小の値を取得
    min_value = min(ans.values())

    # 最小値を持つすべてのキーをリストとして取得
    min_keys = [k for k, v in ans.items() if v == min_value]

    print(len(min_keys))

    for i in range(len(min_keys)):
        print(min_keys[i])

else:
    print(0)