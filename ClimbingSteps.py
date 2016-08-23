class Solution(object):

    def __init__(self) :
        self.d=dict()

    def climbStairs(self, n):

        if n==0 :
            return 0

        self.d[1]=1
        self.d[2]=2

        if n==1 :
            return 1

        if n==2 :
            return 2

        i=3
        while i<=n :
            self.d[i]=self.d[i-2]+self.d[i-1]
            i+=1

        return self.d[n]





            
