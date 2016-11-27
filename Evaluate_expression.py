class Solution(object):

    def evaluateExpression(self,s,evals=dict()) :

      signs=set()
      signs.add('+')
      signs.add('-')
      signs.add('*')
      signs.add('/')

      result=[]

      if len(s)==0 :
          return [0]


      for i in range(0,len(s)) :

        left_values=[]
        right_values=[]

        if s[i] in signs :
          if s[:i] in evals :
            left_values=evals[s[:i]]
          else :
            left_values=self.evaluateExpression(s[:i],evals)
            evals[s[:i]]=left_values

        if s[i+1:] in evals :
          right_values=evals[s[i+1:]]
        else :
          right_values=self.evaluateExpression(s[i+1:],evals)
          evals[s[i+1:]]=right_values

        for val1 in left_values :
         for val2 in right_values :

          if s[i]=='+' :
            res=val1+val2

          if s[i]=='-' :
            res=val1-val2

          if s[i]=='*' :
            res=val1*val2

          if s[i]=='/' :
            res=val1/val2

          result.append(res)


      if len(result)==0 :
       result.append(int(s))

      return result



    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return self.evaluateExpression(input)


        
