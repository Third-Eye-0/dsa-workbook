class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=""
        s=s.lower()
        for i in s:
            if i.isalnum():
                r+=i
        c="".join(reversed(r))
        if c==r:
            return True
        return False