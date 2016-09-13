class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        div=1
        n=x

        if x<0 : return False

        if x<10 : return True

        while n!=0 :
            div*=10
            n/=10

        rev=0
        n=x

        div=div/10

        while x!=0 :
            digit=x%10
            rev+=digit*div
            div=div/10
            x/=10


        return rev==n
        
