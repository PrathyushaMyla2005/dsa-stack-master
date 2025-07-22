"""
LeetCode 394: Decode String
---------------------------

🔗 Problem Link:
https://leetcode.com/problems/decode-string/

📝 Problem:
Given an encoded string, return its decoded version.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
is repeated exactly k times. k is guaranteed to be a positive integer.

You may assume that the input string is always valid — no extra whitespaces, well-formed brackets, etc.

Examples:
---------
Input:  s = "3[a]2[bc]"
Output: "aaabcbc"

Input:  s = "3[a2[c]]"
Output: "accaccacc"

💡 Approach:
We use a *stack* to decode the string from left to right.

- If we find a number → build the full number (could be multi-digit).
- If we find '[' → push the current string and count onto the stack.
- If we find ']' → pop from the stack and multiply the current string.
- If we find a character → add to current string.

This handles *nested encodings* elegantly using stack frames.

⏱ Time Complexity: O(n)
Each character is processed once. String multiplication and concatenation are also O(n) total.

📦 Space Complexity: O(n)
We use a stack to store intermediate strings and counts. In the worst case (deeply nested),
this could require O(n) additional space.
"""
def decode_string(str):
    stack = []
    current_num = 0
    current_str = ""
    for char in str:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            last_str, repeat_count = stack.pop()
            current_str = last_str + current_str * repeat_count
        else:
            current_str += char
    return current_str
if __name__ == "__main__":
    # Example usage
    encoded_str = "3[a2[c]]"
    decoded_str = decode_string(encoded_str)
    print(decoded_str)  # Output: "accaccacc"