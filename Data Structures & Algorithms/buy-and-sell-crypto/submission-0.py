class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        b=prices[0]
        for i in prices:
            p=max(p,i-b)
            b=min(b,i)
        return p