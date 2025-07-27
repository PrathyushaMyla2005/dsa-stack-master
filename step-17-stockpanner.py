"""
✅ Problem Statement: Stock Span Problem
Given a list of daily stock prices, the span of the stock's price on a given day is defined as:
  → the maximum number of consecutive days (starting from that day and going backwards)
     for which the stock price was *less than or equal* to the current day's price.

📥 Input:  prices = [100, 80, 60, 70, 60, 75, 85]
📤 Output: spans  = [1,   1,  1,  2,  1,  4,  6]

✅ Brute Force Approach
🧠 Logic:
For each day i, go backwards and count how many previous days had stock prices
less than or equal to prices[i]. Include the current day itself.

🔁 Outer loop → for each day
🔁 Inner loop → go back until price is greater

⏱ Time Complexity: O(n²) – Worst case: checking each day against all previous days
🧠 Space Complexity: O(n) – To store the span array
"""
#brute_force approach
class StockSpanner:
    def __init__(self):
        self.prices = []

    def next(self, price):
        self.prices.append(price)
        span = 1
        i = len(self.prices) - 2

        while i >= 0 and self.prices[i] <= price:
            span += 1
            i -= 1

        return span

if __name__ == "__main__":
    s = StockSpanner()
    prices = [100, 80, 60, 70, 60, 75, 85]
    for price in prices:
        print(s.next(price))
#optimal approach
class stockspanner:
    def __init__(self):
        self.stack = []
    def next(self, price):
        span = 1
        while self.stack  and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
            self.stack.append((price, span))
            return span
if __name__ == "__main__":
    s = stockspanner()
    print(s.next(100))
    print(s.next(80))
    print(s.next(75))
    print(s.next(90))
    print(s.next(12))
    print(s.next(22))
