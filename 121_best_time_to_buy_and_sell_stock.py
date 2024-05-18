class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            if prices[right] - prices[left] > profit:
                profit = prices[right] - prices[left]
            right += 1

        return profit

