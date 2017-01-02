class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1=map(int,version1.split('.'))
        l2=map(int,version2.split('.'))

        i=0
        j=0
        while i<len(l1) and j<len(l2) :

            if l1[i]>l2[j] :
                return 1

            if l1[i]==l2[j] :
                i+=1
                j+=1

            else :
                return -1


        if i==len(l1) and j==len(l2) : return  0

        if i==len(l1) :

            while j<len(l2) :
                if l2[j]!=0 :
                    return -1
                j+=1

            return 0

        while i<len(l1) :

            if l1[i]!=0 :
                return 1
            i+=1

        return 0





            
