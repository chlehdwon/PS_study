n = int(input())
ans = [i-1 for i in range(n+1)]
prev = [-1] * (n+1)

def solve(n):
    ans[0] = 0
    prev[0] = 1
    for i in range(1,n+1):
        if i+1<=n and ans[i+1] >= ans[i]+1:
            ans[i+1] = ans[i]+1
            prev[i+1] = i
        if 2*i<=n and ans[2*i] >= ans[i]+1:
            ans[2*i] = ans[i]+1
            prev[2*i] = i
        if 3*i<=n and ans[3*i] >= ans[i]+1:
            ans[3*i] = ans[i]+1
            prev[3*i] = i
    
def main():
    solve(n)
    print(ans[n])
    number = n
    for _ in range(ans[n]+1):
        print(number,end=" ")
        number = prev[number]

main()