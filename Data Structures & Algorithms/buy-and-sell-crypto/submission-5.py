class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """maximum = float('-inf')
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                curr_profit = prices[j]-prices[i]
                maximum=max(curr_profit, maximum)
        return max(maximum, 0)"""
        # Sliding window
        minimum = prices[0]
        maximum_profit = float('-inf')
        for i in range(1, len(prices)):
            minimum=min(prices[i], minimum)
            maximum_profit=max(prices[i]-minimum, maximum_profit)
        return max(maximum_profit, 0)
            