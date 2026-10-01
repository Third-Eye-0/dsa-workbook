class Solution:
    def trap(self, h: List[int]) -> int:
        if not h:
            return 0
        l,r=0,len(h)-1
        lm,rm=h[l],h[r]
        re=0
        while l<r:
            if lm<rm:
                l+=1
                lm=max(lm,h[l])
                re+=lm-h[l]
            else:
                r-=1
                rm=max(rm,h[r])
                re+=rm-h[r]
        return re