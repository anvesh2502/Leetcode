# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self,end,start=0):
        """
        :type n: int
        :rtype: int
        """

        if start>end : return -1
        if start==end :
            if isBadVersion(start) : return start
            return -1


        mid=(start+end)/2

        if isBadVersion(mid) :

            if mid>0 :
                if not isBadVersion(mid-1) :
                    return mid
                else :
                    return self.firstBadVersion(mid-1,start)
            else : return mid

        else :

            if mid<end :
                if isBadVersion(mid+1) :
                    return mid+1
                else :
                    return self.firstBadVersion(end,mid+2)
            else :
                if isBadVersion(mid) : return mid
                return -1









        
