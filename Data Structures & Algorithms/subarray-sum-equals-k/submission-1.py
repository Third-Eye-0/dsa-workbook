class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        r=0
        c=0
        p={0:1}
        for i in nums:
            c+=i
            d=c-k
            r+=p.get(d,0)
            p[c]=1+p.get(c,0)
        return r