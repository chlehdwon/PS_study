"""
Given a characters array tasks, representing the tasks a CPU needs to
do, where each letter represents a different task. Tasks could be done
in any order. Each task is done in one unit of time. For each unit of
time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown
period between two same tasks (the same letter in the array), that is
that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to
finish all the given tasks.
"""


import collections
import heapq
from typing import List


from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # create list of process occurances
        occurances = list(Counter(tasks).values())

        # base interval calculation = # of groups * size of each group
        intervals = (max(occurances)-1) * (n+1)
        # account for remaining intervals from processes with most occurances
        count_procc_with_max = occurances.count(max(occurances))
        # add these to your total interval count
        intervals += count_procc_with_max

        # return max of calculated intervals and length of initials task list
        return max(intervals, len(tasks))


class Solution2:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = collections.Counter(tasks)
        # list which contains the list of executable work
        works = []
        # list which contains the list of works have to wait
        wait = collections.deque()
        for char, num in c.items():
            heapq.heappush(works, [-num, 0, char])
        num = 0
        while works or wait:
            num += 1
            # move work data from 'wait' to 'works' if the work wait for n
            if wait and wait[0][1] + n < num:
                heapq.heappush(works, wait.popleft())
            # if there is excutable works, then do and update
            if works:
                job_info = heapq.heappop(works)
                job_info[0] += 1
                job_info[1] = num
                if job_info[0] < 0:
                    wait.append(job_info)

        return num


class Solution3:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            # extract works in counter order
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1

                counter.subtract(task)
                # delete not positive elements in the list
                counter += collections.Counter()

            if not counter:
                break

            result += n - sub_count + 1

        return result
