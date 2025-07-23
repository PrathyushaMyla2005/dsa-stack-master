class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        # Iterate through each digit
        for digit in num:
            # Remove larger digits from the stack if possible
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # Remove remaining digits from the end if k > 0
        while k > 0:
            stack.pop()
            k -= 1

        # Construct final result and strip leading zeros
        result = ''.join(stack).lstrip('0')
        return result or '0'


# 🧪 Example Usage
if __name__ == "__main__":
    num = "1432219"
    k = 3
    solution = Solution()
    print("Input Number:", num)
    print("Digits to Remove:", k)
    print("Resulting Number:", solution.removeKdigits(num, k))
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""