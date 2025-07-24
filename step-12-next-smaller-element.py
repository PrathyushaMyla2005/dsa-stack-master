# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def nextSmallerElement(self, height):
        stack = []
        result = [-1] * len(height)  # Initialize result with -1 for all elements

        for i in range(len(height)-1, -1, -1):  # Traverse from right to left
            while stack and stack[-1] >= height[i]:
                stack.pop()  # Pop elements that are not smaller
            if stack:
                result[i] = stack[-1]  # The next smaller element
            stack.append(height[i])  # Push current element to stack

        return result

# ✅ Run the function with example input
if __name__ == "__main__":
    obj = Solution()
    height = [4, 8, 5, 2, 25]
    print("Next Smaller Elements:", obj.nextSmallerElement(height))
