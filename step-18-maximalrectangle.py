#  time complexity: O(m * n) where m is the number of rows and n is the number of columns in the matrix.
#  space complexity: O(n) for the heights array and stack.
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        n_cols = len(matrix[0])
        heights = [0] * n_cols
        max_area = 0

        for row in matrix:
            # Update heights
            for i in range(n_cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0

            # Calculate max area for current histogram row
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(0)  # Add sentinel for flush

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        heights.pop()  # Remove sentinel
        return max_area


if __name__ == "__main__":
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    
    sol = Solution()
    print(sol.maximalRectangle(matrix))  # Expected output: 6
