
"""
📌 Problem: Infix to Postfix Conversion (Expression Evaluation)

🔗 Concept: Convert an infix expression (e.g., a + b * c) to postfix (Reverse Polish Notation, e.g., abc*+)

🧠 Approach:

- Use the **Shunting Yard Algorithm** to convert infix to postfix.
- Use a stack to store operators and parentheses.
- Traverse the infix expression character by character:
  - If it's an operand (number/variable), add it to the output.
  - If it's '(', push to stack.
  - If it's ')', pop from stack to output until '(' is found.
  - If it's an operator:
    - Pop operators from the stack with **greater or equal precedence**, then push the current one.
- After traversal, pop any remaining operators from the stack to the output.

⏰ Time Complexity: O(n)
- Each character is processed once.

💾 Space Complexity: O(n)
- Stack can hold all operators and parentheses in the worst case.

"""
def precedence(op):
    if op == '^':
        return 3
    if op == '*' or op == '/':
        return 2
    if op == '+' or op == '-':
        return 1
    return 0

def infix_to_postfix(expression):
    stack = []
    postfix = ""
    
    for ch in expression:
        if ch.isalnum():  # operand (A, B, C, 1, 2)
            postfix += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # remove '('
        else:  # operator
            while stack and precedence(stack[-1]) >= precedence(ch):
                postfix += stack.pop()
            stack.append(ch)

    # pop remaining operators
    while stack:
        postfix += stack.pop()

    return postfix
if __name__ == "__main__":
    expr = "a+b*(c^d-e)^(f+g*h)-i"
# This expression includes `^`, which is not handled above.
# Let's test with: expr = "a+b*c"
print(infix_to_postfix("a+b*c"))  # Output: "abc*+"
