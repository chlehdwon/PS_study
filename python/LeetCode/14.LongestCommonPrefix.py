# Write a function to find the longest common prefix string
# amongst an array of strings.
# If there is no common prefix, return an empty string "".


class Solution:
    def longestCommonPrefix(self, strs):
        pre = ""
        if strs:
            stand, check = strs[0], 1
            for i in range(0, len(stand)):
                for str in strs:
                    if stand[:i+1] != str[:i+1]:
                        check = 0
                        break
                if check and str == strs[-1]:
                    pre = stand[:i+1]
                elif not check:
                    break
        return pre


a = Solution()
print(a.longestCommonPrefix(["flower", "flow", "flight"]))
