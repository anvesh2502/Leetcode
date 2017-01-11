class Solution(object):

    def get_sqrt(self,low,high,x) :


        mid=(low+high)/2

        if (mid*mid)==x :
            return mid

        if (mid*mid)>x :

            if low>mid-1 :
                return mid-1

            return self.get_sqrt(low,mid-1,x)

        if (mid+1)>high :
            return mid

        return self.get_sqrt(mid+1,high,x)




    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 : return 0
        if x==1 : return 1

        return self.get_sqrt(1,x/2,x)
