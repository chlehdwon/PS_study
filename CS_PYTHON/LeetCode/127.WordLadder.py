# Given two words (beginWord and endWord), and
# a dictionary's word list, find the length of shortest transformation
# sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.


from collections import defaultdict
from collections import deque


# BFS Algorithm Solution
# Time Complexity : O(M^2*N),
# where M is the length of the words and N is the lentgth of word list.
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        L = len(beginWord)
        # We make a dictionary which contains all possible transform
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        # We use deque because popleft is O(1) in deque.
        # While, just queue is O(n).
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        # if the word in the visited map, we skip the word,
        # i.e. don't append the word into the queue.
        # if the word not in the visited map, we put the word into
        # the map, and append the word into the queue.
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
        return 0


a = Solution()
print(a.ladderLength(beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
))
