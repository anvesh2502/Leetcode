class Solution(object):
    def integerReplacement(self,n):
        """
        :type n: int
        :rtype: int
        """
        if n==1 : return 0
        if n==2 : return 1
        if n==3 : return 2

        if n%2==0 :
            return 1+self.integerReplacement(n/2)

        l=1+self.integerReplacement(n+1)
        r=1+self.integerReplacement(n-1)

        return min(l,r)
            
