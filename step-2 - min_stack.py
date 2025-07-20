"""
📌 Problem: Min Stack (LeetCode #155)
-------------------------------------

🧠 Design a stack that supports:
- push(x)
- pop()
- top()
- getMin() — all in O(1) time

📈 Time Complexity:
- push: O(1)
- pop: O(1)
- top: O(1)
- getMin: O(1)

📦 Space Complexity:
- O(n)

🛠 Approach:
Use two stacks:
1. main_stack: to store all elements
2. min_stack: to store current minimums
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Fix: previously you overwrote self.stack

    def push(self, x):
        self.stack.append(x)
        # Push to min_stack if empty or x is less than or equal to current min
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
 
    def pop(self):
        if self.stack:
            popped = self.stack.pop()
            # Pop from min_stack if it is the minimum
            if popped == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return "stack is underflow"

    def getMin(self):  # Fix: capital 'M' to match LeetCode's `getMin`
        if self.min_stack:
            return self.min_stack[-1]
        return "stack is underflow"


# Testing
if __name__ == "__main__":  # Fix: remove space between "__" and "main__"
    s = MinStack()
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)
    s.push(10)
    print("Min:", s.getMin())  # Min should be 10
    s.pop()                    # Remove 10
    print("Min:", s.getMin())  # Min should be 20
    print("Top:", s.top())     # Top should be 50
    print("Min:", s.getMin())  # Min should be 20
