"""
There are n gas stations along a circular route, where the amount of
gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas
to travel from the ith station to its next (i + 1)th station. You begin
the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas
station's index if you can travel around the circuit once in the
clockwise direction, otherwise return -1. If there exists a solution,
it is guaranteed to be unique
"""


from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas or sum(gas) < sum(cost):
            return -1
        gas[0] = gas[0] - cost[0]
        # update values to amount of gas when we start from 0
        for i in range(1, len(gas)):
            gas[i] = gas[i-1] + gas[i] - cost[i]
        min_index = 0
        # find index which the value is minimum
        for i in range(1, len(gas)):
            if gas[min_index] > gas[i]:
                min_index = i
        # return the next index of min_index
        return min_index + 1 if min_index < len(gas) - 1 else 0


class Solution2:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        gas_at = [0 for i in range(len(gas))]
        start = 0
        for i in range(1, len(gas)):
            gas_at[i] = gas_at[i-1] + gas[i-1] - cost[i-1]
            if gas_at[i] < gas_at[start]:
                start = i
        return start


# LeetCode's Answer. It is more faster that mine.
# Difference point is that this solution doesn't create the list
# Instead of creating list, it initialize the amount of gas
# when it goes to negative. And memorize that point.
# The last point is minimum point, which is the answer.

class Solution3:
    def canCompleteCircuit(self, gas, cost):
        if (sum(gas) - sum(cost) < 0):
            return -1

        gas_tank, start_index = 0, 0

        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]

            if gas_tank < 0:
                start_index = i+1
                gas_tank = 0

        return start_index

