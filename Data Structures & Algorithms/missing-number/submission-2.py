class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)  # Start with 'n'
        
        for i, num in enumerate(nums):
            res ^= i ^ num  # XOR the index and the actual number
            
        return res
