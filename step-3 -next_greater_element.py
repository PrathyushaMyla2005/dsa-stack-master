"""
🔹 Problem: Next Greater Element
Given an array, find the Next Greater Element (NGE) for every element.
The Next Greater Element for an element x is the first greater element
on the right side of x in the array. If no greater element exists, output -1.

📦 Time Complexity: O(n)
📦 Space Complexity: O(n)
💡 Approach: Monotonic Stack (Decreasing Stack)
"""
def next_greater_element(arr):
    stack = []
    n = len(arr)
    res = [-1]*n
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            res[index] = arr[i]
        stack.append(i)
    return res
if __name__ == "__main__":
    arr = [4, 5, 2, 10, 8]
    print("Input Array:", arr)
    print("Next Greater Element:", next_greater_element(arr))