class Solution(object):
    def multiply(self, num1, num2,units=0):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if len(num1)==0 or len(num2)==0 :
            return '0'

        if num1=='0' or num2=='0' :
            return '0'

        end=len(num2)-1
        n=int(num2[end])
        carry=0
        j=len(num1)-1
        res=''

        while j>=0 :

            prod=n*int(num1[j])+carry
            if prod>9 :
                carry=prod/10
                prod=prod%10

            else :
                carry=0
            res=str(prod)+res
            j-=1


        if carry!=0 :
            res=str(carry)+res


        res=int(res)*int('1'+('0'*units))

        num2=num2[0:end]


        total=res+int(self.multiply(num1,num2,units+1))


        return str(total)







        
