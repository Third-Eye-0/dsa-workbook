from collections import Counter as counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=counter(nums)
        for i in s:
            if s[i]>1:
                return True
        return False
