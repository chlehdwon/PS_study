"""
A character in UTF8 can be from 1 to 4 bytes long, subjected to the
following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0,
followed by n-1 bytes with most significant 2 bits being 10.
"""


from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        return True