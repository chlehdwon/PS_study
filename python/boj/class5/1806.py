import sys

n, target = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

min_len = n+1
start, end, sum = 0, 0, array[0]

while end < n:
    if sum >= target:
        min_len = min(min_len, end - start + 1)
        sum -= array[start]
        start += 1
        continue
    else:
        end += 1
        if end < n:
            sum += array[end]
        continue

print(min_len if min_len != n+1 else 0)