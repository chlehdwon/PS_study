# Given a string s, partition s such that every substring of the partition
# is a palindrome. Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.


# This is DFS answer by usgin backtracking
# Time complexity is O(N*2^N)

class Solution:
    def partition(self, s: str):
        res = []
        self.backtrack(s, start=0, path=[], res=res)
        return res

    def backtrack(self, s, start, path, res):
        print(start, path, res)
        # If we reach last of the str, then put partitions to the res.
        if start == len(s):
            res.append(path)
            return

        for end in range(start + 1, len(s) + 1):
            # If we find the palindrome, then start backtracking
            # from the next index.
            sub = s[start: end]
            if sub == sub[::-1]:
                self.backtrack(s, end, path + [sub], res)


a = Solution()
print(a.partition("aaaa"))
