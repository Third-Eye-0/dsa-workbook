class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m=1
        while(True):
            f=True
            for i in nums:
                if m==i:
                    f=False
                    break
            if f:
                return m
            m+=1
