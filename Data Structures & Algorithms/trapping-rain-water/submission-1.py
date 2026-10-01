class Solution:
    def trap(self, h: List[int]) -> int:
        if not h:
            return 0
        l=0
        r=len(h)-1
        lm=h[l]
        rm=h[r]
        re=0
        while(l<r):
            if lm<rm:
                l+=1
                lm=max(lm,h[l])
                re+=lm-h[l]
            else:
                r-=1
                rm=max(rm,h[r])
                re+=rm-h[r]
        return re