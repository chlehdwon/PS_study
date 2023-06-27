"""
Implement a trie with insert, search, and startsWith methods.
"""


import collections


# TrieNode
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Word Insertion
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    # Search the word in the trie
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.word

    # decide any word starts with the prefix is exist in the trie
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True
