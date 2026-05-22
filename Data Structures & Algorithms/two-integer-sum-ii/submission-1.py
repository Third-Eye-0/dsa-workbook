class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m=defaultdict(int)
        for i in range(len(nums)):
            t=target-nums[i]
            if m[t]:
                return [m[t],i+1]
            m[nums[i]]=i+1
        return []