class Solution(object):


    def getcode(self,s) :

        d=dict()
        for c in s :

         d.setdefault(c,1)
         d[c]+=1

        res=''

        keys=sorted(d)

        for k in keys :
            res+=k+''+str(d[k])
        return res



    def groupAnagrams(self, strs):

        d=dict()

        for str in strs :
            val=self.getcode(str)
            d.setdefault(val,[])
            d[val].append(str)

        result_list=[]

        for k in d :
            result_list.append(d[k])
        return result_list







        
