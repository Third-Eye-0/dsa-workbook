class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=0
        n=len(nums)
        for i in range(n):
            while(1<=nums[i]<=n and nums[i]!=nums[nums[i]-1]):
                c=nums[i]-1
                nums[c],nums[i]=nums[i],nums[c]
        for i in range(n):
            if nums[i]!=i+1: return i+1
        return n+1
            