def solve(n, k):
    if n < k*(k+1)//2:
        print(-1)
    else:
        print(k) if (n - k*(k+1)//2) % k else print(k-1)


n, k = map(int, input().split())
solve(n, k)
