
class Solution:
    def merge(self, nums, l,m,r):
        n1=m-l+1
        n2=r-m
        L=[0]*n1
        R=[0]*n2
        for i in range(n1):
            L[i]=nums[l+i]
        for j in range(n2):
            R[j]=nums[m+1+j]
        i=0;j=0;k=l
        while(i<n1 and j<n2):
            if(L[i]<=R[j]):
                nums[k]=L[i]
                k+=1;i+=1
            else:
                nums[k]=R[j]
                k+=1;j+=1
        while(i<n1):
            nums[k]=L[i]    
            k+=1;i+=1
        while(j<n2):
            nums[k]=R[j]
            k+=1;j+=1


    def mergesort(self, nums, l,r):
        if(l<r):
            m=int((l+r)/2)
            self.mergesort(nums,l,m)
            self.mergesort(nums,m+1,r)
            self.merge(nums,l,m,r)
    def sortArray(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        self.mergesort(nums,l,r)
        return nums
        