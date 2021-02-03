"""
Given a non-empty array of integers nums, every element appears twice
except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime
complexity and without using extra memory?
"""


from collections import defaultdict

# I use hashtable by create defaultdict.
# Time complexity is linear, but space complexity is O(n).


class Solution:
    def singleNumber(self, nums):
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1

        for i in hash_table:
            if hash_table[i] == 1:
                return i

# To make O(1) space complexity, we use XOR.
        # APPROACH : XOR ##

        # TIME COMPLEXITY : O(N) ##
        # SPACE COMPLEXITY : O(1) ##

        # If we take XOR of zero and some bit, it will return that bit
        # a XOR 0 = a, a XOR 0=a
        # If we take XOR of two same bits, it will return 0
        # a XOR a = 0 a XOR a=0
        # a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b
        # a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
        # So we can XOR all bits together to find the unique number.


class Solution2:
    def singleNumber(self, nums):
        single_num = 0
        for num in nums:
            single_num ^= num
        return single_num

