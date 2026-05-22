class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1
        while i<j:
            c=nums[i]+nums[j]
            if(c==target):
                return[i+1,j+1]
            elif c > target:
                j-=1
            else:
                i+=1
        return []