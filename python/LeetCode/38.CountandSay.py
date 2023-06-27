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
        elif n == 2:
            return "11"
        else:
            prev = self.countAndSay(n-1)
            say = ""
            target = prev[0]
            nums = 0
            for i in prev[:-1]:
                if i != target:
                    say += str(nums) + target
                    target = i
                    nums = 1
                else:
                    nums += 1
            if prev[-1] == target:
                nums += 1
                say += str(nums) + target
            else:
                say += str(nums) + target + '1' + prev[-1]
            return say


class Solution2:
    def countAndSay(self, n: int) -> str:
        output = '1'
        for i in range(2, n+1):
            res = ''
            cur = output[0]
            count = 1
            for x in output[1:]:
                if x == cur:
                    count += 1
                else:
                    res += str(count) + cur
                    count = 1
                    cur = x
            res += str(count) + cur
            output = ''.join(res)
        return output


a = Solution()
print(a.countAndSay(10))
