import sys

def bsearch(target, arr):
    left, right = 0, len(arr)-1
    while left<right:
        mid = (left+right)//2
        if arr[mid]==target:
            return 1 
        elif arr[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return int(arr[left]==target)

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
targets = list(map(int,sys.stdin.readline().split()))

nums.sort()
for target in targets:
    print(bsearch(target, nums))

