class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        S=Counter(s)
        T=Counter(t)
        f=True
        for i in s:
            if(S[i]!=T[i]):
                f = False
                break
        return f