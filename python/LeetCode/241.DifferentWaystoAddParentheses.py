"""
Given a string of numbers and operators, return all possible results
from computing all the different possible ways to group numbers and
operators. The valid operators are +, - and *.
"""


from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        if input[i] == '+':
                            res.append(l+r)
                        elif input[i] == '-':
                            res.append(l-r)
                        elif input[i] == '*':
                            res.append(l*r)
        return res


class Solution2:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results

        if input.isdigit():
            return [int(input)]

        results = []
        for index, value in enumerate(input):
            if value in "-+*":
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index + 1:])

                results.extend(compute(left, right, value))
        return results
