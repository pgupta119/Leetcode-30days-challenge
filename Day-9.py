# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit return 0.


# My solution :

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        current_diff = 0
        for i in range(0,len(prices)):
            for j in range (i+1,len(prices)):
                if prices[i]< prices[j]:
                    current_diff = prices[j] -prices[i]
                if current_diff> max_diff:
                    max_diff =current_diff
        if max_diff >=0:
            return max_diff
        else:
            return 0
# TIME COMPLEXITY 0(N*N)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        for i in range(0,len(prices)-1):
            for j in range (i+1,len(prices)):
                price = prices[j] - prices[i]
                if price > max_diff:
                    max_diff = price
        return max_diff


# optimal solution :

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit




