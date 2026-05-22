class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        n=int(n/3)
        r=[]
        c=Counter(nums)
        for i in c:
            if c[i]>n:
                r.append(i)
        return r
