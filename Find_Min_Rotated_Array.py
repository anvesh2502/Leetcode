class Solution(object):


    def findMin(self, a,low=0,high=0):
        """
        :type nums: List[int]
        :rtype: int
        """
        if low==0 and high==0 :
            low=0
            high=len(a)-1


        if low>high :
            return a[0]


        mid=(low+high)/2
        
        if mid==0 :
            return self.findMin(a,mid+1,high)

        if a[mid-1]>a[mid] and a[mid]<a[0] :
            return a[mid]

        if a[mid-1]<a[mid] and a[mid]>a[0]:
            return self.findMin(a,mid+1,high)

        return self.findMin(a,low,mid-1)
