# Determine whether an integer is a palindrome.
# An integer is a palindrome when it reads the same backward as forward.async


class Solution:
    def isPalindrome(self, x):
        pal = 0
        x1 = x
        while x > 0:
            pal = pal * 10 + x % 10
            x = x // 10
            if pal == x1:
                return True
        return not x1

    def isPalindrome_f(self, x):
        return str(x) == str(x)[::-1]


a = Solution()
print(a.isPalindrome(121))
print(a.isPalindrome(-121))
print(a.isPalindrome(10))
print(a.isPalindrome(1001))
print(a.isPalindrome(0))
