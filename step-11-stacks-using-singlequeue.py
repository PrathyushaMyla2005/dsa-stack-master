"""
📌 Problem: Implement Stack using a Single Queue
🔗 LeetCode: https://leetcode.com/problems/implement-stack-using-queues/

🧠 Approach:
- Use a single queue (FIFO) to simulate stack (LIFO) behavior.
- After pushing a new element, rotate the queue to bring it to the front.

⏰ Time Complexity:
- push: O(n)
- pop, top, empty: O(1)

💾 Space Complexity: O(n)
"""
from collections import deque
class mystack:
    def __init__(self):
        self.queue = deque()
    def push(self,x):
        self.queue.append(x)
        # Rotate the queue to make the new element the front
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
    def pop(self):
        return self.queue.popleft() 
    def top(self):
        return self.queue[0]
    def empty(self):
        return len(self.queue) == 0
# Example usage:
if __name__ == "__main__":
    stack = mystack()
    stack.push(1)
    stack.push(2)
    print(stack.top())  # Output: 2
    print(stack.pop())  # Output: 2
    print(stack.empty())  # Output: False
    print(stack.pop())  # Output: 1
    print(stack.empty())  # Output: True
    stack.push(3)
    print(stack.top())  # Output: 3
