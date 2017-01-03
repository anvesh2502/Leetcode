class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack=[]
        return_str=''

        for c in s :

            if c!=']' :
                stack.append(c)

            else :

                s=''
                p=''
                while p!='[' :
                    s+=p
                    p=stack.pop()

                n=stack.pop()
                num=''+n
                while len(stack)!=0  :
                    n=stack.pop()

                    if not n.isdigit() :
                        stack.append(n)
                        break

                    num+=n

                num=num[::-1]

                num=int(num)

                s=s[::-1]*num



                for c in s :
                    stack.append(c)



        return ''.join(stack)




        
