class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = float('-inf')
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                curr_profit = prices[j]-prices[i]
                maximum=max(curr_profit, maximum)
        return max(maximum, 0)
            