class Solution:
    def maxArea(self, h: List[int]) -> int:
        i,j=0,len(h)-1
        m=0
        while(i<j):
            a=min(h[i],h[j])*((j-i))
            m=max(a,m)
            if h[i]<=h[j]:
                i+=1
            else:
                j-=1
        return m