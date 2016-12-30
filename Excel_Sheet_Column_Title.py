class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n<=0 : return ""

        if n<=26 :

            return chr(ord('A')+n-1)

        div=n/26



        if div==1 :
            return 'A'+chr(ord('A')+(n%26)-1)

        else :
            rem=(n%26-1)%26
            if (n%26)!=0 :
             return self.convertToTitle(div)+chr(ord('A')+rem)
            else :
             return self.convertToTitle(div-1)+chr(ord('A')+rem)









            
