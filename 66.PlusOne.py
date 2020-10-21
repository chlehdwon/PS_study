# Given a non-empty array of digits representing a non-negative integer,
# increment one to the integer.

# The digits are stored such that the most significant digit
# is at the head of the list, and each element in the array contains
# a single digit.

# You may assume the integer does not contain any leading zero,
# except the number 0 itself.

class Solution:
    def plusOne(self, digits):
        length = len(digits)
        carry = 0
        digits[-1] += 1
        for i in range(length):
            digits[length-1-i] += carry
            if digits[length-1-i] >= 10:
                digits[length-1-i] -= 10
                carry = 1
            else:
                carry = 0
        if digits[0] == 0:
            return [1]+digits
        return digits

class Solution2:
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i]!=9:
                digits[i]+=1
                break
            else:
                digits[i]=0
                if i==0:
                    digits.insert(0,1)
        return digits


a = Solution2()
print(a.plusOne([4,3,2,1]))