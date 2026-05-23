class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a,2)
        y=int(b,2)
        c=a+y
        return f"{c:b}"