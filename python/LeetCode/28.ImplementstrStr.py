# Implement strStr().

# Return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        if len(needle) == 0:
            return 0
        haystack_len = len(haystack)
        first_occurr= []
        for i in range(0, haystack_len-needle_len+1):
            if needle[0] == haystack[i]:
                first_occurr.append(i)
        if not first_occurr:
            return -1
        for i in first_occurr:
            if needle == haystack[i:i+needle_len]:
                return i
        return -1


class Solution2:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


a = Solution()
print(a.strStr("hello", ""))