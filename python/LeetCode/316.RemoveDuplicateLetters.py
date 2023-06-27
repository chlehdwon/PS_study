import collections

"""
Given a string s, remove duplicate letters so that every letter appears
once and only once. You must make sure your result is the smallest in
lexicographical order among all possible results.
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # sort letters by using set
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            # if suffix set is same as entire set, seperate them.
            if set(s) == set(suffix):
                return char +                                         self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''


class Solution2:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # if there is any letter which can put at the end, then delete it from the stack
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)
