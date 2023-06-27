# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary
# until the first non-whitespace character is found. Then, starting from
# this character takes an optional initial plus or minus sign followed by
# as many numerical digits as possible, and interprets them as a numerical
# value.
# The string can contain additional characters after those that form the
# integral number, which are ignored and have no effect on the behavior of
# this function.
# If the first sequence of non-whitespace characters in str is not a valid
# integral number, or if no such sequence exists because either str is
# empty or it contains only whitespace characters, no conversion is
# performed.
# If no valid conversion could be performed, a zero value is returned.


class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        num = 0
        blank = 0
        plusminus = 0
        s.strip()
        for i in s:
            if i == " " and blank == 0:
                continue
            elif i == '-':
                if sign == -1 or plusminus == 1:
                    if num != 0:
                        return num*sign
                    else:
                        return 0
                else: 
                    blank = 1
                    plusminus = 1
                    sign = -1
            elif i == '+':
                if sign == -1 or plusminus == 1:
                    if num != 0:
                        return num*sign
                    else:
                        return 0
                else: 
                    blank = 1
                    plusminus = 1
            elif ord(i) >= ord('0') and ord(i) <= ord('9'):
                num = num * 10 + ord(i) - ord('0')
                blank = 1
                plusminus = 1
                if sign == -1 and num > 2147483648:
                    return -2147483648
                elif sign == 1 and num > 2147483647:
                    return 2147483647
            else:
                return num*sign
        return num*sign


class Solution2:
    MAPPING = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "0": 0,
    }

    MAX_INT = 2**31-1
    MIN_INT = -(2**31)
    def myAtoi(self, string: str) -> int:
        s = string.lstrip(' ')
        if not s:
            return 0
        
        sign = -1 if s[0] == "-" else 1
        if sign != 1 or s[0] == "+":
            s = s[1:]
            
        res = 0
        for c in s:
            if c not in MAPPING:
                return self.limit(res * sign)
            
            res *= 10
            res += MAPPING[c]
            
        return self.limit(res * sign)
    
    def limit(self, x: int) -> int:
        if x > MAX_INT:
            return MAX_INT
        if x < MIN_INT:
            return MIN_INT
        return x


a = Solution()
# print(a.myAtoi("4193 with words"))
# print(a.myAtoi("words and 987"))
print(a.myAtoi("00000-42a1234"))
# print(a.myAtoi("-91283472332"))
