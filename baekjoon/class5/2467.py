from math import inf

n = int(input())
x = list(map(int,input().split()))

def binary_search_right(target):
    left, right = 0, n-1
    while left<right:
        mid = (left+right)//2
        if target==x[mid]:
            return mid
        elif target>x[mid]:
            left = mid+1
        else:
            right=mid
    return left

if x[-1]<=0:
    print(x[-2], x[-1])
elif x[0]>=0:
    print(x[0], x[1])
else:
    min_value, base, acid = inf, 0, 0
    for i,target in enumerate(x):
        idx = binary_search_right(-target)
        if idx>0 and (x[idx]==target or (abs(target+x[idx])>abs(target+x[idx-1]))) and x[idx-1]!=target:
            idx=idx-1
        if min_value > abs(target+x[idx]):
            base, acid = min(x[idx], target), max(x[idx],target)
            min_value = abs(target+x[idx])
            if min_value==0:
                break
    print(base, acid)

            
###
# 다음과 같이 2-pointer로도 해결 가능하다!
# from math import inf

# n = int(input())
# x = list(map(int,input().split()))

# def binary_search_right(target):
#     left, right = 0, n-1
#     while left<right:
#         mid = (left+right)//2
#         if target==x[mid]:
#             return mid
#         elif target>x[mid]:
#             left = mid+1
#         else:
#             right=mid
#     return left

# if x[-1]<=0:
#     print(x[-2], x[-1])
# elif x[0]>=0:
#     print(x[0], x[1])
# else:
#     min_value, base, acid = inf, 0, 0
#     for i,target in enumerate(x):
#         idx = binary_search_right(-target)
#         if idx>0 and (x[idx]==target or (abs(target+x[idx])>abs(target+x[idx-1]))) and x[idx-1]!=target:
#             idx=idx-1
#         if min_value > abs(target+x[idx]):
#             base, acid = min(x[idx], target), max(x[idx],target)
#             min_value = abs(target+x[idx])
#             if min_value==0:
#                 break
#     print(base, acid)

            
            
    

