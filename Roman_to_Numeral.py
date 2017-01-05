class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=dict()
        d['I']=1
        d['V']=5
        d['X']=10
        d['L']=50
        d['C']=100
        d['D']=500
        d['M']=1000

        prev=None
        total=0

        for c in s :

            if not prev :
                total+=d[c]
            else :
                if d[prev]>=d[c] :
                    total+=d[c]
                else :
                    total+=d[c]-2*d[prev]

            prev=c


        return total








            
