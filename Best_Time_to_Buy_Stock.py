class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        d=dict()
        for i in range(0,len(prices)) :
            d[prices[i]]=i

        max_array=[]
        i=len(prices)-1
        max_val=-1

        while i>0 :
            max_val=max(prices[i],max_val)
            max_array.append(max_val)
            i-=1

        max_array.reverse()
        diff=-1

        for i in range(0,len(prices)-1) :
            rel=max_array[i]-prices[i]
            if diff<rel :
                diff=rel

        if diff==-1 : diff=0

        return diff

        
