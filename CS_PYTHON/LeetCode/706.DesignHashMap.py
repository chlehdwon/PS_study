"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap.
If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped,
or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key
if this map contains the mapping for the key.
"""


import collections


# Definition for singly-linked list.
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    # initiallizing
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    # insert
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # if no node in index, just put and return
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # if there is node in index, link them by linkedlist
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    # get
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        # if there is node, then find the node
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # delete
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # delete process when first node is the target
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # delete linkedlist node
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
