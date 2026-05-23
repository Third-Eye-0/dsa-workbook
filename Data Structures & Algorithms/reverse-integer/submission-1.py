class Solution:
    def reverse(self, x: int) -> int:
        min = -2147483648
        max = 2147483647
        res=0
        s= -1 if x < 0 else 1
        x=abs(x)
        while x:
            digit=int(x%10)
            x//=10
            if res>max//10 or (res==max//10 and digit>max%10):
                return 0
            if res<min//10 or (res==min//10 and digit<min%10):
                return 0
            res=(res*10)+digit
        res*=s
        return res