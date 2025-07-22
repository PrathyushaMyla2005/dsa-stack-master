"""
LeetCode 735: Asteroid Collision
--------------------------------

🔗 Problem Link:
https://leetcode.com/problems/asteroid-collision/

📝 Problem:
Given an array asteroids representing asteroids in a row. 
- The absolute value represents size.
- The sign represents direction:
    - Positive → right-moving
    - Negative → left-moving

All asteroids move at the same speed. When two asteroids meet:
- The smaller one explodes.
- If both are the same size, both explode.
- Asteroids moving in the same direction will never meet.

Return the state of the asteroids after all collisions.

Example:
---------
Input:  asteroids = [5, 10, -5]
Output: [5, 10]

Explanation:
10 and -5 collide → 10 survives, -5 explodes.

💡 Approach:
We use a stack to simulate asteroid movements and handle collisions:
- Push asteroid if:
    - Stack is empty
    - Asteroid is moving right
    - Top of stack is moving left
- If current asteroid is moving left and top is moving right:
    - Compare sizes:
        - If current is larger: pop top, repeat check
        - If equal: pop top, discard current
        - If smaller: discard current

⏱ Time Complexity: O(n)  
📦 Space Complexity: O(n)
"""
from typing import List

class Solution:
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # This will store indices

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                result[prev_idx] = i - prev_idx
            stack.append(i)

        return result

if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    solution = Solution()
    print(solution.daily_temperatures(temperatures))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
