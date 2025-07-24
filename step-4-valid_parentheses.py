"""
🔹 Problem: Valid Parentheses
Check if the input string of brackets is valid or not.

📦 Time Complexity: O(n)
📦 Space Complexity: O(n)
💡 Approach: Use Stack to match opening and closing brackets
"""
class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping: # closing bracket like ')', '}', ']'
                # Pop the top element if stack is not empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(char)

        # If stack is empty, all brackets matched
        return not stack

if __name__ == "__main__":
    s = Solution()
    test_str = "()[]{}"
    print(s.isValid(test_str))  # Output: True
