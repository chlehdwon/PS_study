# Given a string, determine if it is a palindrome,
# considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem,
# we define empty string as valid palindrome


class Solution:
    def isPalindrome(self, s):
        alnum = ""
        for str in s.lower():
            if str.isalnum():
                # isalnum() retruns True
                # if the string only contain alphanumeric letters
                # if not, return False
                alnum += str
        return alnum == alnum[::-1]

    def isPalindrome_f(self, s):
        # More faster by using filter()
        alnum = filter(str.isalnum, s.lower())
        alphanumeric = "".join(alnum)
        return alphanumeric == alphanumeric[::-1]


a = Solution()
print(a.isPalindrome("A man, a plan, a canal: Panama"))
print(a.isPalindrome("race a car"))
print(a.isPalindrome_f("A man, a plan, a canal: Panama"))
print(a.isPalindrome_f("race a car"))
