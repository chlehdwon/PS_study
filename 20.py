# Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: boolean
        :my code
        """
        p_pair = {')': '(', '}': '{', ']': '['}
        p_dict = {'(': [], '{': [], '[': []}
        for i, p in enumerate(list(s)):
            if p in p_pair.values():
                p_dict[p].append(i)
            elif p in p_pair.keys():
                a = p_dict[p_pair[p]]
                if len(a) == 0:
                    return False
                j = a.pop()
                for nums in p_dict.values():
                    for num in nums:
                        if num in range(j, i):
                            return False
        for i in p_dict.values():
            if len(i) != 0:
                return False
        return True

    def isValid_f(self, s):
        """
        :type s: str
        :rtype: boolean
        :fastest code
        """
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []


a = Solution()
print(a.isValid("(]"))
print(a.isValid_f("(]"))
