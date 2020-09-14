# Given n pairs of parentheses, write a function
# to generate all combinations of well-formed parentheses.


class Solution:
    def generateParenthesis(self, n):
        paren_set = set()
        paren_dict = {}
        if n == 1:
            paren_set.add("()")
        else:
            i = 1
            while i <= n/2:
                if i in paren_dict:
                    paren_a = paren_dict[i]
                else:
                    paren_dict[i] = paren_a = self.generateParenthesis(i)
                if n-i in paren_dict:
                    paren_b = paren_dict[n-i]
                else:
                    paren_dict[n-i] = paren_b = self.generateParenthesis(n-i)
                for a in paren_a:
                    for b in paren_b:
                        paren_set.add(a+b)
                        paren_set.add(b+a)
                i += 1
            a = paren_dict[n-1]
            for s in a:
                paren_set.add("("+s+")")
        return list(paren_set)


class Solution_2:
    def generateParenthesis(self, n):
        res = []
        self.helper(n, n, res=res)
        return res

    def helper(self, open_parens: int, closed_parens: int, curr='',
               res=[]):
        if open_parens == 0 and closed_parens == 0:
            res.append(curr)
            return

        if open_parens > 0:
            self.helper(open_parens - 1, closed_parens, curr + '(', res)

        if open_parens < closed_parens:
            self.helper(open_parens, closed_parens - 1, curr + ')', res)


a = Solution()
# b = Solution_2()
print(sorted(a.generateParenthesis(4)))
# print(sorted(b.generateParenthesis(6)))
