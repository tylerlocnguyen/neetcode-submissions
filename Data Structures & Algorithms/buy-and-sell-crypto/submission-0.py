class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        result = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
                right = left + 1
            else:
                result = max(result, prices[right] - prices[left])
                right += 1
        return result