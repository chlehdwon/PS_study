import sys

# LIS를 O(nlogn)으로 구하는 알고리즘.
# 우리가 원하는 정답 vector를 이진탐색을 통해 만들어나가는 방법
# vector가 실제 LIS가 아니기 때문에 index를 따로 정리해야 한다.
#   index를 따로 정리한 후, 뒤에서부터 처음으로 해당 길이의 index를 갖는 원소만 뽑아낸다.

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
vector, index = [array[0]], [0]

def lower_bound(lo, hi, target):
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if vector[mid] >= target:
            hi = mid
        else:
            lo = mid
    return hi

for num in array[1:]:
    if vector[-1] < num:
        vector.append(num)
        index.append(len(vector)-1)
    else:
        idx = lower_bound(-1, len(vector), num)
        vector[idx] = num
        index.append(idx)

lis, idx = [], len(vector)-1
for i in range(len(array)-1, -1, -1):
    if index[i] == idx:
        lis.append(array[i])
        idx -= 1

print(len(vector))
print(" ".join(list(map(str, lis[::-1]))))
