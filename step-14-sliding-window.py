
"""📌 Problem: 239. Sliding Window Maximum

🔗 LeetCode: https://leetcode.com/problems/sliding-window-maximum/

🧠 Approach:

- Use a deque to efficiently maintain a list of candidate maximum indices.
- Remove indices that are:
  - Outside the current sliding window
  - Smaller than the current number (since they can't be the max anymore)
- The front of the deque always holds the index of the maximum for the current window.
- Append that maximum to the result once the first window is fully formed.

⏰ Time Complexity: O(n)
- Each element is pushed and popped from the deque at most once.

💾 Space Complexity: O(k)
- Deque holds at most k indices at any time.

"""
from collections import deque

def maximumSlidingWindow(nums, k):
    n = len(nums)
    result = []
    d = deque()  # This stores indices, not values

    for i in range(n):
        # Step 1: Remove indices that are out of the current window
        while d and d[0] < i - k + 1:
            d.popleft()
        
        # Step 2: Remove indices whose corresponding values are less than nums[i]
        while d and nums[d[-1]] < nums[i]:
            d.pop()
        
        # Step 3: Add the current index
        d.append(i)
        
        # Step 4: Append the maximum value of the current window to result
        if i >= k - 1:
            result.append(nums[d[0]])
    
    return result
if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maximumSlidingWindow(nums, k))
