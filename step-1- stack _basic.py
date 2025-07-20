"""
📌 Stack Basics Implementation in Python
----------------------------------------

🧠 Description:
This file contains the basic implementation of the stack data structure using a Python list.

👨‍💻 Operations Supported:
- push(item): Add an element to the top of the stack.
- pop(): Remove and return the top element.
- peek(): View the top element without removing it.
- is_empty(): Check if the stack is empty.
- size(): Return the current size of the stack.

📈 Time Complexity:
- push: O(1)
- pop: O(1)
- peek: O(1)
- is_empty: O(1)
- size: O(1)

📦 Space Complexity:
- O(n), where n is the number of elements in the stack.

✅ Written for product-based company interview preparation.
"""
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "underflow"

    def peak(self):
        if not self.is_empty():
            return self.stack[-1]
        return "underflow"

    def is_empty(self):
        return len(self.stack) == 0    

    def size(self):
        return len(self.stack)

if __name__ == "__main__":
    s = Stack()
    s.push(777)
    s.push(333)
    s.push(111)
    
    print(s.pop())      
    print(s.peak())      
    print(s.is_empty()) 
    print(s.size())
