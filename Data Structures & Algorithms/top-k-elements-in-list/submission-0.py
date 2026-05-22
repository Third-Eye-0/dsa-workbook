class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        d=d.most_common()
        d=dict(d)
        l=list(d.keys())
        return l[:k]