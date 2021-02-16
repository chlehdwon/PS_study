"""
Given a string s, find the length of the longest substring
without repeating characters.
"""


class Solution:
    # the book's solution.
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # if it appear before, update the index of 'start'
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:  # updete the length of longest substring
                max_length = max(max_length, index - start + 1)

            # insert index of current character
            used[char] = index

        return max_length


class Solution2:
    # my first solution. It is very impressive that runtime is very short.
    def lengthOfLongestSubstring(self, s):
        subs = ""
        max_len = len(list(set(s)))
        longest_len, index, length, point = 0, 0, 0, 0
        for i, str in enumerate(s):
            if subs.find(str) != -1:
                point = subs.find(str)
                length = len(subs)
                if length == max_len:
                    return length
                if length > longest_len:
                    longest_len = length
                index = index + point + 1
                subs = s[index:i+1]
            else:
                subs += str
                if len(subs) > longest_len:
                    longest_len = len(subs)
        return longest_len


class Solution3:
    # Leetcode's answer. Similar to solution 1.
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict = {}
        max_len = 0
        max_max_len = len(list(set(s)))
        k = 0
        for i, j in enumerate(s):
            if j in my_dict:
                if k <= my_dict[j]:
                    k = my_dict[j]+1
            sub_ss = s[k:i+1]
            max_len = max(len(sub_ss), max_len)
            if max_len == max_max_len:
                return max_len
            my_dict[j] = i
        return max_len


a = Solution()
print(a.lengthOfLongestSubstring("pwwkewabcde"))
print(a.lengthOfLongestSubstring_f("pwwkewabcde"))
