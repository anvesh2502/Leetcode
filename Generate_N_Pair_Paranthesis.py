class Solution(object):


    def genPar(self,s) :
        if s=='()' :
         return ['()']

        prefix='()'
        rest=s[2:]


        perms=self.genPar(rest)
        out=set()


        for p in perms :


         for i in range(0,len(p)+1) :
            new=p[0:i]+prefix+p[i:]
            out.add(new)


        l=[]

        for result in out :
            l.append(result)

        return l




    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.genPar('()'*n)




        
