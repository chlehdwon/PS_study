# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is
# given below. Note that 1 does not map to any letters.


class Solution:
    def letterCombinations(self, digits):
        ntol = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        length = len(digits)
        idxs = [0 for i in range(length)]
        idxs_len = [len(ntol[digits[i]])-1 for i in range(length)]
        com = []
        if digits:
            while True:
                letter = ''
                if idxs != idxs_len:
                    for i in range(length):
                        num = ntol[digits[i]]
                        idx = idxs[i]
                        letter += num[idx]
                    com.append(letter)
                    idxs[0] += 1
                    for i in range(length-1):
                        num = ntol[digits[i]]
                        if idxs[i] == idxs_len[i]+1:
                            idxs[i] = 0
                            idxs[i+1] += 1
                else:
                    for i in range(length):
                        num = ntol[digits[i]]
                        idx = idxs[i]
                        letter += num[idx]
                    com.append(letter)
                    break
        return com

        def letterCombinations_2(self, digits):
            if not digits:
                return []
            dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
            ans = [[]]
            letters = tuple(tuple(dic[x]) for x in digits)
            for letter in letters:
                ans = [x + [y] for x in ans for y in letter]
            return [''.join(ele) for ele in ans]


class Solution_2:
    def __init__(self):
        self.nums = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'],
                     "4": ['g', 'h', 'i'],
                     "5": ['j', 'k', 'l'], "6": ['m', 'n', 'o'],
                     "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'],
                     "9": ['w', 'x', 'y', 'z'], }

    def letterCombinations(self, digits):
        if not digits:
            return []
        res = []
        for letter in self.nums[digits[0]]:
            res.extend(
                [letter+i for i in self.letterCombinations(digits[1:])]
                or [letter])
        return res


a = Solution()
print(a.letterCombinations("23"))
b = Solution_2()
print(b.letterCombinations("23"))
