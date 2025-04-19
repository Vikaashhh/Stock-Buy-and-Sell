from typing import List

class Solution:
    def maximumProfit(self, prices: List[int]) -> int:
        profit = 0  # Total profit ko store karne ke liye variable

        # Har din ke price ko previous din se compare karenge
        for i in range(1, len(prices)):
            # Agar agle din ka price zyada hai to uss din sell karke profit le sakte hain
            if prices[i] > prices[i - 1]:
                # Profit me difference add kar denge
                profit += prices[i] - prices[i - 1]

        return profit  # Final profit return karenge
    

if __name__ == "__main__":
    prices = [100, 180, 260, 310, 40, 535, 695]
    solution = Solution()
    print("Maximum Profit:", solution.maximumProfit(prices))  # Output: 865