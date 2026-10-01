class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        c=c.most_common()
        c=dict(c)
        c=list(c.keys())
        return c[:k]