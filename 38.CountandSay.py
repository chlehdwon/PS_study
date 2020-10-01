# The count-and-say sequence is the sequence of integers
# with the first five terms as following:
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the
# count-and-say sequence.You can do so recursively, in other words from
# the previous member read off the digits, counting the number of digits
# in groups of the same digit.


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            prev = self.countAndSay(n-1)
            say = ""
            print(n, prev)
            target = prev[0]
            nums = 1
            for i in prev:
                if i != target:
                    say += str(nums) + target
                    target = i
                    nums = 1
                else:
                    nums += 1
            print(say)
            return say


a = Solution()
print(a.countAndSay(2))
