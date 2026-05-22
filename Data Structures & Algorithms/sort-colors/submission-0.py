class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        m=max(nums)
        count=[0]*(m+1)
        for i in range(n):
            count[nums[i]]+=1
        index=0
        for i in range(len(count)):
            while(count[i]!=0):
                nums[index]=i
                count[i]-=1
                index+=1
            


