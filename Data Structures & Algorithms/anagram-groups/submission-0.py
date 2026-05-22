class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            c=[0]*26
            for j in s:
                c[ord(j)-ord('a')]+=1
            res[tuple(c)].append(s)  
        return list(res.values())          