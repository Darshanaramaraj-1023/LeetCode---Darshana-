# Last updated: 8/11/2026, 4:01:56 PM
class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        total=0.0
        for i in range(min(len(prices),len(discounts))):
            total+=prices[i]*(100 - discounts[i])/100
        for i in range(len(discounts),len(prices)):
            total+=prices[i]
        return total
        
        