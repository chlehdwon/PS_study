import sys

# LIS를 O(nlogn)으로 구하는 알고리즘.
# 우리가 원하는 정답 vector를 이진탐색을 통해 만들어나가는 방법
# 배열을 돌면서 다음과 같은 연산을 진행
#   vec의 마지막 값보다 배열의 값이 크다면 vec 뒤에다 추가
#   아니라면, 이진 탐색을 통해 lower bound 위치에 값을 배열의 값으로 변경
#   ex) vector가 [10, 20, 25, 50], num=30이면, vector를 [10, 20, 25, 30]으로 변경
# 참고로 이 경우는 길이 밖에 구할 수 없음.
#   배열 상에는 뒤에 있지만, lower_bound를 통해 vector 상에서 앞에 있을수도 있기 때문.

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
vector = [array[0]]

def binary_search(start, end, target):
    if start >= end:
        return end
    mid  = (start + end) // 2
    if target == vector[mid]:
        return mid
    elif target > vector[mid]:
        return binary_search(mid+1, end, target)
    else:
        return binary_search(start, mid, target) 

for num in array[1:]:
    if vector[-1] < num:
        vector.append(num)
    elif vector[0] > num:
        vector[0] = num
    else:
        idx = binary_search(0, len(vector)-1, num)
        vector[idx] = num

print(len(vector))

# 내장 함수를 사용하여 더 빨리 풀었음
"""
def solution():
    import sys
    from bisect import bisect_left

    nums = map(int, sys.stdin.read().rstrip().split())
    next(nums)
    lis = [next(nums)]

    for n in nums:
        if lis[-1] < n:
            lis.append(n)
        else:
            lis[bisect_left(lis, n)] = n

    print(len(lis))

solution()
"""