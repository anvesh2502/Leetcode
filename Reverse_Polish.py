class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack=[]

        for token in tokens :


            if token in ['+','-','*','/'] :

                if len(stack)<2 :
                    continue
                else :
                    b=int(stack.pop())
                    a=int(stack.pop())
                    if token=='+' :
                        print a+b
                        stack.append(a+b)
                    if token=='-' :
                        print a-b
                        stack.append(a-b)

                    if token=='*' :
                        print a*b
                        stack.append(a*b)

                    if token=='/' :
                         if a<0 and b<0 :
                             a*=-1
                             b*=-1
                             stack.append(a/b)

                         elif a<0 :
                             a*=-1
                             stack.append((-1)*(a/b))

                         elif b<0 :
                             b*=-1
                             stack.append((-1)*(a/b))
                         else :
                             stack.append(a/b)






            else :
                stack.append(int(token))

        if len(stack)==1 :
                return stack.pop()


        
