"""
🔹 Problem: Evaluate Reverse Polish Notation
📦 Time Complexity: O(n)
📦 Space Complexity: O(n)
💡 Approach: Use a stack to evaluate tokens
"""
class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Python division truncates toward negative infinity, but
                    # we need it to truncate toward zero like in LeetCode
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]
sol = Solution()
print(sol.evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9
print(sol.evalRPN(["4", "13", "5", "/", "+"]))  # Output: 6
print(sol.evalRPN(["10", "6", "9", "3", "/", "-", "*"]))  # Output: 60
 