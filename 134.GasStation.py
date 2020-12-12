# There are N gas stations along a circular route, where the amount of gas
# at station i is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to
# travel from station i to its next station (i+1).
# You begin the journey with an empty tank at one of the gas stations.

# Return the starting gas station's index if you can travel around the
# circuit once in the clockwise direction, otherwise return -1.


# Find the index which means when the car has the most less oil.
# Set that index as the start point.

class Solution:
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
# Difference point is that this solution doesn't create the liest.abs()
# Instead of creating list, it initialize the amount of gas
# when it goes to negative. And memorize that point.
# The last point is minimum point, which is the answer.

class Solution2:
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


a = Solution()
print(a.canCompleteCircuit(gas  = [1,2,3,4,5]
, cost = [3,4,5,1,2]))