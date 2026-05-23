class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=""
        c=0
        a,b=a[::-1],b[::-1]
        for i in range(max(len(a),len(b))):
            da = int(a[i]) if i<len(a) else 0
            db = ord(b[i])-ord("0") if i<len(b) else 0
            t=da+db+c
            ch=str(t%2)
            res=ch+res
            c=t//2
        if c:
            res="1"+res
        return res