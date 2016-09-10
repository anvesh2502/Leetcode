class Solution(object):
    def isUgly(self, num,cycle=False):
        """
        :type num: int
        :rtype: bool
        """

        if num==0  :
            return cycle

        l=[2,3,5]

        if num in l : return True

        if num==1 : return True





        for v in l :
            if num%v==0 and self.isUgly(num/v,True) :
                return True

        return False
        
