class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r=defaultdict(list)
        for i in strs:
            c=[0]*26
            for j in i:
                c[ord(j)-ord('a')]+=1
            r[tuple(c)].append(i)
        return list(r.values())
