class Solution(object):



    def get_combinations(self,ans,index=0) :

        if index>=len(ans)-1 :

            return list(ans[index])

        next_combs=self.get_combinations(ans,index+1)

        chars=list(ans[index])
        result=[]

        for c1 in chars :
            for c2 in next_combs :
                s=c1+c2
                result.append(s)


        return result















    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone={2:"abc",3:"def",4 : "ghi",5 : "jkl",6: "mno",7 : "pqrs",8 : "tuv",9 : "wxyz"}

        ans=[]

        if digits=="" :
            return []



        for c in digits :
            ans.append(phone[int(c)])

        print ans


        return self.get_combinations(ans)    
