class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        c=c.most_common()
        c=dict(c)
        l=list(c.keys())
        return l[:k]
