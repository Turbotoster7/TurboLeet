class Solution:
    def maxIceCream(self, costs, coins) -> int:
        costs.sort()
        amount = 0
        for cost in costs:
            if coins < cost:
                return amount
            coins -= cost
            amount += 1 

        return amount
    
costs = [1,6,3,1,2,5]
coins = 20
s = Solution()
s.maxIceCream(costs, coins)