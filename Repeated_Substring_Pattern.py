class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type str: str
        :rtype: bool
        """

        n=len(s)

        for i in range(1,(n/2)+1) :

            if (n%i)==0 :
                sub=s[:i]
                div=n/(len(sub))
                if s==(sub*div) :
                    return True


        return False





        
