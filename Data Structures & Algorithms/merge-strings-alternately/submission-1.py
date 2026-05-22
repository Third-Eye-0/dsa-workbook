class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        k=0
        r=""
        while(i<len(word1) and j<len(word2)):
            if(k%2==0):
                r+=word1[i]
                k+=1
                i+=1
            else:
                r+=word2[j]
                k+=1
                j+=1
        while(i<len(word1)):
            r+=word1[i]
            i+=1
        while(j<len(word2)):
            r+=word2[j]
            j+=1
        return r