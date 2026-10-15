class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        local_min = 100
        profit = 0

        # prices = [10,1,5,6,7,1]
        # lm = 1

        for price in prices:
            if price < local_min:
                local_min = price
            transaction = price - local_min
            if transaction > profit:
                profit = transaction
        
        return profit

