"""
✅ Problem Statement: Celebrity Problem

You're given a matrix M of size n x n such that:
- M[i][j] = 1 means person i knows person j
- M[i][j] = 0 means person i doesn't know person j

A celebrity is someone who:
1. Is known by everyone.
2. Knows no one.

🧠 Conditions for Celebrity:
- M[celebrity][j] == 0 for all j ≠ celebrity → Celebrity knows no one.
- M[i][celebrity] == 1 for all i ≠ celebrity → Everyone knows the celebrity.
"""

# ✅ Naive Approach
# ⏱ Time Complexity: O(n^2)
# 🧠 Space Complexity: O(1)
def find_celebrity_naive(M, n):
    for i in range(n):
        knows_someone = False
        known_by_all = True
        for j in range(n):
            if i != j:
                if M[i][j] == 1:
                    knows_someone = True
                if M[j][i] == 0:
                    known_by_all = False
        if not knows_someone and known_by_all:
            return i
    return -1


# ✅ Optimized Two Pointer Approach
# ⏱ Time Complexity: O(n)
# 🧠 Space Complexity: O(1)
def find_celebrity_two_pointer(M, n):
    celeb = 0
    for i in range(1, n):
        if M[celeb][i] == 1:
            celeb = i
    for i in range(n):
        if i != celeb:
            if M[celeb][i] == 1 or M[i][celeb] == 0:
                return -1
    return celeb


# ✅ Stack Approach
# ⏱ Time Complexity: O(n)
# 🧠 Space Complexity: O(n)
def find_celebrity_stack(M, n):
    stack = list(range(n))
    while len(stack) > 1:
        A = stack.pop()
        B = stack.pop()
        if M[A][B] == 1:
            stack.append(B)
        else:
            stack.append(A)
    if not stack:
        return -1
    celebrity = stack.pop()
    for i in range(n):
        if i != celebrity:
            if M[celebrity][i] == 1 or M[i][celebrity] == 0:
                return -1
    return celebrity


# ✅ Driver Code to Test All Approaches
if __name__ == "__main__":
    matrices = [
        [[0, 1, 0], [0, 0, 0], [1, 1, 0]],      # Celebrity at index 1
        [[0, 1, 0], [1, 0, 1], [1, 1, 0]]       # No celebrity
    ]

    for idx, M in enumerate(matrices, 1):
        n = len(M)
        print(f"\n🔍 Test Case {idx}")

        # Naive
        result = find_celebrity_naive(M, n)
        print(f"Naive: Celebrity is person {result}" if result != -1 else "Naive: No celebrity found")

        # Two Pointer
        result = find_celebrity_two_pointer(M, n)
        print(f"Two Pointer: Celebrity is person {result}" if result != -1 else "Two Pointer: No celebrity found")

        # Stack
        result = find_celebrity_stack(M, n)
        print(f"Stack: Celebrity is person {result}" if result != -1 else "Stack: No celebrity found")
"""
✅ Problem Statement: Celebrity Problem

You're given a matrix M of size n x n such that:
- M[i][j] = 1 means person i knows person j
- M[i][j] = 0 means person i doesn't know person j

A celebrity is someone who:
1. Is known by everyone.
2. Knows no one.

🧠 Conditions for Celebrity:
- M[celebrity][j] == 0 for all j ≠ celebrity → Celebrity knows no one.
- M[i][celebrity] == 1 for all i ≠ celebrity → Everyone knows the celebrity.
"""

# ✅ Naive Approach
# ⏱ Time Complexity: O(n^2)
# 🧠 Space Complexity: O(1)
def find_celebrity_naive(M, n):
    for i in range(n):
        knows_someone = False
        known_by_all = True
        for j in range(n):
            if i != j:
                if M[i][j] == 1:
                    knows_someone = True
                if M[j][i] == 0:
                    known_by_all = False
        if not knows_someone and known_by_all:
            return i
    return -1


# ✅ Optimized Two Pointer Approach
# ⏱ Time Complexity: O(n)
# 🧠 Space Complexity: O(1)
def find_celebrity_two_pointer(M, n):
    celeb = 0
    for i in range(1, n):
        if M[celeb][i] == 1:
            celeb = i
    for i in range(n):
        if i != celeb:
            if M[celeb][i] == 1 or M[i][celeb] == 0:
                return -1
    return celeb


# ✅ Stack Approach
# ⏱ Time Complexity: O(n)
# 🧠 Space Complexity: O(n)
def find_celebrity_stack(M, n):
    stack = list(range(n))
    while len(stack) > 1:
        A = stack.pop()
        B = stack.pop()
        if M[A][B] == 1:
            stack.append(B)
        else:
            stack.append(A)
    if not stack:
        return -1
    celebrity = stack.pop()
    for i in range(n):
        if i != celebrity:
            if M[celebrity][i] == 1 or M[i][celebrity] == 0:
                return -1
    return celebrity


# ✅ Driver Code to Test All Approaches
if __name__ == "__main__":
    matrices = [
        [[0, 1, 0], [0, 0, 0], [1, 1, 0]],      # Celebrity at index 1
        [[0, 1, 0], [1, 0, 1], [1, 1, 0]]       # No celebrity
    ]

    for idx, M in enumerate(matrices, 1):
        n = len(M)
        print(f"\n🔍 Test Case {idx}")

        # Naive
        result = find_celebrity_naive(M, n)
        print(f"Naive: Celebrity is person {result}" if result != -1 else "Naive: No celebrity found")

        # Two Pointer
        result = find_celebrity_two_pointer(M, n)
        print(f"Two Pointer: Celebrity is person {result}" if result != -1 else "Two Pointer: No celebrity found")

        # Stack
        result = find_celebrity_stack(M, n)
        print(f"Stack: Celebrity is person {result}" if result != -1 else "Stack: No celebrity found")
"""
✅ Problem Statement: Celebrity Problem

You're given a matrix M of size n x n such that:
- M[i][j] = 1 means person i knows person j
- M[i][j] = 0 means person i doesn't know person j

A celebrity is someone who:
1. Is known by everyone.
2. Knows no one.

🧠 Conditions for Celebrity:
- M[celebrity][j] == 0 for all j ≠ celebrity → Celebrity knows no one.
- M[i][celebrity] == 1 for all i ≠ celebrity → Everyone knows the celebrity.
"""

# ✅ Naive Approach
# ⏱ Time Complexity: O(n^2)
# 🧠 Space Complexity: O(1)
def find_celebrity_naive(M, n):
    for i in range(n):
        knows_someone = False
        known_by_all = True
        for j in range(n):
            if i != j:
                if M[i][j] == 1:
                    knows_someone = True
                if M[j][i] == 0:
                    known_by_all = False
        if not knows_someone and known_by_all:
            return i
    return -1


# ✅ Optimized Two Pointer Approach
# ⏱ Time Complexity: O(n)
# 🧠 Space Complexity: O(1)
def find_celebrity_two_pointer(M, n):
    celeb = 0
    for i in range(1, n):
        if M[celeb][i] == 1:
            celeb = i
    for i in range(n):
        if i != celeb:
            if M[celeb][i] == 1 or M[i][celeb] == 0:
                return -1
    return celeb


# ✅ Stack Approach
# ⏱ Time Complexity: O(n)
# 🧠 Space Complexity: O(n)
def find_celebrity_stack(M, n):
    stack = list(range(n))
    while len(stack) > 1:
        A = stack.pop()
        B = stack.pop()
        if M[A][B] == 1:
            stack.append(B)
        else:
            stack.append(A)
    if not stack:
        return -1
    celebrity = stack.pop()
    for i in range(n):
        if i != celebrity:
            if M[celebrity][i] == 1 or M[i][celebrity] == 0:
                return -1
    return celebrity


# ✅ Driver Code to Test All Approaches
if __name__ == "__main__":
    matrices = [
        [[0, 1, 0], [0, 0, 0], [1, 1, 0]],      # Celebrity at index 1
        [[0, 1, 0], [1, 0, 1], [1, 1, 0]]       # No celebrity
    ]

    for idx, M in enumerate(matrices, 1):
        n = len(M)
        print(f"\n🔍 Test Case {idx}")

        # Naive
        result = find_celebrity_naive(M, n)
        print(f"Naive: Celebrity is person {result}" if result != -1 else "Naive: No celebrity found")

        # Two Pointer
        result = find_celebrity_two_pointer(M, n)
        print(f"Two Pointer: Celebrity is person {result}" if result != -1 else "Two Pointer: No celebrity found")

        # Stack
        result = find_celebrity_stack(M, n)
        print(f"Stack: Celebrity is person {result}" if result != -1 else "Stack: No celebrity found")
"""
✅ Problem Statement: Celebrity Problem

You're given a matrix M of size n x n such that:
- M[i][j] = 1 means person i knows person j
- M[i][j] = 0 means person i doesn't know person j

A celebrity is someone who:
1. Is known by everyone.
2. Knows no one.

🧠 Conditions for Celebrity:
- M[celebrity][j] == 0 for all j ≠ celebrity → Celebrity knows no one.
- M[i][celebrity] == 1 for all i ≠ celebrity → Everyone knows the celebrity.
"""


# ✅ Naive Approach
# ⏱ Time Complexity: O(n^2)
# 🧠 Space Complexity: O(1)
def find_celebrity_naive(M, n):
    for i in range(n):
        knows_someone = False
        known_by_all = True
        for j in range(n):
            if i != j:
                if M[i][j] == 1:
                    knows_someone = True
                if M[j][i] == 0:
                    known_by_all = False
        if not knows_someone and known_by_all:
            return i
    return -1


# ✅ Optimized Two Pointer Approach
# ⏱ Time Complexity: O(n)
# 🧠 Space Complexity: O(1)
def find_celebrity_two_pointer(M, n):
    celeb = 0
    for i in range(1, n):
        if M[celeb][i] == 1:
            celeb = i
    for i in range(n):
        if i != celeb:
            if M[celeb][i] == 1 or M[i][celeb] == 0:
                return -1
    return celeb


# ✅ Stack Approach
# ⏱ Time Complexity: O(n)
# 🧠 Space Complexity: O(n)
def find_celebrity_stack(M, n):
    stack = list(range(n))
    while len(stack) > 1:
        A = stack.pop()
        B = stack.pop()
        if M[A][B] == 1:
            stack.append(B)
        else:
            stack.append(A)
    if not stack:
        return -1
    celebrity = stack.pop()
    for i in range(n):
        if i != celebrity:
            if M[celebrity][i] == 1 or M[i][celebrity] == 0:
                return -1
    return celebrity


# ✅ Driver Code to Test All Approaches
if __name__ == "__main__":
    matrices = [
        [[0, 1, 0], [0, 0, 0], [1, 1, 0]],      # Celebrity at index 1
        [[0, 1, 0], [1, 0, 1], [1, 1, 0]]       # No celebrity
    ]

    for idx, M in enumerate(matrices, 1):
        n = len(M)
        print(f"\n🔍 Test Case {idx}")

        # Naive
        result = find_celebrity_naive(M, n)
        print(f"Naive: Celebrity is person {result}" if result != -1 else "Naive: No celebrity found")

        # Two Pointer
        result = find_celebrity_two_pointer(M, n)
        print(f"Two Pointer: Celebrity is person {result}" if result != -1 else "Two Pointer: No celebrity found")

        # Stack
        result = find_celebrity_stack(M, n)
        print(f"Stack: Celebrity is person {result}" if result != -1 else "Stack: No celebrity found")
