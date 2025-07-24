"""

        📌 Problem: Sum of All Subarrays

        🔗 LeetCode: https://leetcode.com/problems/sum-of-all-subarrays/



        🧠 Approach:

        - Use a single loop to calculate the sum of all subarrays.

        - For each element, calculate its contribution to the total sum based on its position.



        ⏰ Time Complexity: O(n)

        💾 Space Complexity: O(1)

        """
class solution:
    def sumofallsubarrays(self,arr):
        n = len(arr)
        total_sum =0
        for i in range(n):
            #contribution of arr[i] to the total sum
            contribution = arr[i] * (i+1) * (n-i)
            total_sum += contribution
        return total_sum
# Example usage:
if __name__ == "__main__":
    obj = solution()
    arr = [1, 2, 3]
    print("Sum of All Subarrays:", obj.sumofallsubarrays(arr))  # Output: 20