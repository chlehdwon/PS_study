"""
Implement a first in first out (FIFO) queue using only two stacks. The
implemented queue should support all the functions of a normal queue
(push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
"""


class MyQueue:
    # using 2 stacks. push is O(1), and pop is O(n)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = []
        self.s = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.m.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.m) > 1:
            self.s.append(self.m.pop())
        p = self.m.pop()
        while self.s:
            self.m.append(self.s.pop())
        return p

    def peek(self) -> int:
        """
        Get the front element.
        """
        while len(self.m) > 1:
            self.s.append(self.m.pop())
        t = self.m[0]
        while self.s:
            self.m.append(self.s.pop())
        return t

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.m) == 0


class MyQueue2:
    # using 2 stacks. push is O(1), and pop is amortized O(1)
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        # if output is empty, then insert them all into output
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
