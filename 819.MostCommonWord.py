import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

"""
Given a paragraph and a list of banned words, return the
most frequent word that is not in the list of banned words.
It is guaranteed there is at least one word that isn't
banned, and that the answer is unique.

Words in the list of banned words are given in lowercase,
and free of punctuation.  Words in the paragraph are not
case sensitive.  The answer is in lowercase.
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        wordcounter = collections.defaultdict(int)
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                 if word not in banned]
        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1
        return max(counts, key=counts.get)


class Solution2:
    # another solution without re
    def mostCommonWord(self, paragraph, banned):
        counter = {}
        max_cnt = 0
        max_word = ''
        banned = set(banned)
        new_paragraph = []
        word = ''
        for symbol in paragraph:
            if symbol.isalpha():
                word += symbol.lower()
            elif word:
                if word not in banned:
                    if counter.get(word):
                        counter[word] += 1
                    else:
                        counter[word] = 1
                    if counter[word] > max_cnt:
                        max_cnt = counter[word]
                        max_word = word
                word = ''
        if max_word:
            return max_word 
        else:
            return word