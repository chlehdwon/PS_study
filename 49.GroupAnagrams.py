# Given an array of strings strs, group the anagrams together. You can
# return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters
# exactly once.

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        group_dict = {}
        for i in strs:
            str_sorted = ''.join(sorted(i))
            if str_sorted not in group_dict:
                group_dict[str_sorted] = [i]
            else:
                group_dict[str_sorted].append(i)
        return list(group_dict.values())


class Solution2:
    def groupAnagrams(self, strs):
        group_dict = defaultdict(list)
        for i in strs:
            group_dict[''.join(sorted(i))].append(i)
        return list(group_dict.values())


a = Solution2()
print(a.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(a.groupAnagrams([""]))
print(a.groupAnagrams(["a"]))