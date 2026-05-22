class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i,v in enumerate(nums):
            d=target-v
            if(d in a):
                return [a[d],i]
            a[v]=i