import sys

def find_parent(x):
    while x != parent[x]:
        x = parent[x]
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    # parent가 높은쪽으로 합쳐줌
    if a < b:
        parent[b] = a
        return False
    elif a > b:
        parent[a] = b
        return False
    else:
        return True


n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n)]

def solve():
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if union_parent(a, b):
            print(i+1)
            return
    print(0)
    return

solve()

### rank를 통해 tree 최적화 가능
# import sys

# input = sys.stdin.readline


# def find(x):
#     if x != parent[x]:
#         parent[x] = find(parent[x])  # 재귀를 돌며 해당 부모를 최상위 노드로 설정
#     return parent[x]

# def union_(a, b):
#     a = find(a)
#     b = find(b)

#     if a == b:
#         return
#     # 만약 랭크 a가 b보다 더 깊다면
#     if rank[a] > rank[b]:
#         parent[b] = a  # b에 a를 붙인다.
#     elif rank[a] < rank[b]:  # 만약 랭크 b가 랭크 a보다 더 깊다면
#         parent[a] = b  # a에 b를 붙인다.
#     else:  # 둘의 랭크가 같다면
#         rank[b] += 1  # b의 랭크깊이를 1개 추가한 뒤
#         parent[a] = b  # b에 a를 붙인다.


# N, M = map(int, input().split())

# parent = [i for i in range(N)]
# rank = [0] * N  # union by rank 처리를 위한 랭크 기록함수
# ans = 0
# for i in range(M):
#     a, b = map(int, input().split())

#     if not ans:  # 답이 아직 나오지 않았다면
#         if find(a) == find(b):  # 만약 싸이클이 형성되어 있다면
#             ans = i + 1  # 해당 순번을 입력
#         else:  # 싸이클이 형성되어있지 않다면
#             union_(a, b)  # 두 노드를 유니온

# print(ans)