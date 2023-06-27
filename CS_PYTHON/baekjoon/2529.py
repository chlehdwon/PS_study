N = int(input())

X = list(input().split())

result = [0]*(N+1)

used = [False]*10

cnt = 0

for i in range(N):
    if X[i] == '<':
        cnt += 1
        if i == N - 1:
            for j in range(cnt + 1):
                for k in range(9, -1, -1):
                    if not used[k]:
                        used[k] = True
                        result[i+1 - j] = k
                        break
    else:
        for j in range(cnt+1):
            for k in range(9, -1, -1):
                if not used[k]:
                    used[k] = True
                    result[i-j] = k
                    break
        if i == N - 1:
            for k in range(9, -1, -1):
                if not used[k]:
                    used[k] = True
                    result[i+1] = k
                    break
        cnt = 0


print(''.join(map(str, result)))

result = [0]*(N+1)

used = [False]*10

cnt = 0

for i in range(N):
    if X[i] == '>':
        cnt += 1
        if i == N - 1:
            for j in range(cnt + 1):
                for k in range(10):
                    if not used[k]:
                        used[k] = True
                        result[i+1 - j] = k
                        break
    else:
        for j in range(cnt+1):
            for k in range(10):
                if not used[k]:
                    used[k] = True
                    result[i-j] = k
                    break
        if i == N - 1:
            for k in range(10):
                if not used[k]:
                    used[k] = True
                    result[i+1] = k
                    break
        cnt = 0


print(''.join(map(str, result)))
