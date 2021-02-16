# Roman numerals are represented by seven different symbols
# : I, V, X, L, C, D and M.
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.


class Solution:
    def romanToInt(self, s):
        sym = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        rom_int = 0
        for i in range(0, len(s)):
            num = sym[s[i]]
            if i < len(s)-1 and num < sym[s[i+1]]:
                rom_int -= num
            else:
                rom_int += num
        return rom_int


a = Solution()
print(a.romanToInt("MCMXCIV"))
print(a.romanToInt("IV"))
print(a.romanToInt("M"))
