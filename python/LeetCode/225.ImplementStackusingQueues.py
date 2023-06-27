"""
Implement a last in first out (LIFO) stack using only two queues. The
implemented stack should support all the functions of a normal queue
(push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
"""
import collections


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.main_queue = collections.deque()
        self.sub_queue = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.main_queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for _ in range(len(self.main_queue)-1):
            self.sub_queue.append(self.main_queue.popleft())
        pop = self.main_queue.popleft()
        self.main_queue, self.sub_queue = self.sub_queue, self.main_queue

        return pop

    def top(self) -> int:
        """
        Get the top element.
        """
        for _ in range(len(self.main_queue)-1):
            self.sub_queue.append(self.main_queue.popleft())
        top = self.main_queue.popleft()
        self.sub_queue.append(top)
        self.main_queue, self.sub_queue = self.sub_queue, self.main_queue

        return top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.main_queue) == 0


class MyStack2:
    # 1 queue, push is O(n), pop is O(1)
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        # after append the element, resort elements
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
