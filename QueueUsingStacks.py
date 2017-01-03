class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1=[]
        self.stack2=[]


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """



        if len(self.stack1)==0 and len(self.stack2)==0 :
            self.stack1.append(x)
            return

        if len(self.stack1)==0 :
            self.stack2.append(x)
            return

        self.stack1.append(x)











    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.stack1)==0 and len(self.stack2)==0 :
            return


        if len(self.stack1)==0 :

            while len(self.stack2)!=1 :
                self.stack1.append(self.stack2.pop())

            self.stack2.pop()

            while len(self.stack1)!=0 :
                self.stack2.append(self.stack1.pop())

        else :

            while len(self.stack1)!=1 :
                self.stack2.append(self.stack1.pop())

            self.stack1.pop()

            while len(self.stack2)!=0 :
                self.stack1.append(self.stack2.pop())




    def peek(self):
        """
        :rtype: int
        """
        if len(self.stack1)==0 and len(self.stack2)==0 :
            return -1

        r=-1
        print self.stack1,self.stack2

        if len(self.stack1)==0 :

            while len(self.stack2)!=1 :
                self.stack1.append(self.stack2.pop())

            r=self.stack2[-1]

            while len(self.stack1)!=0 :
                self.stack2.append(self.stack1.pop())

            self.stack2.append(r)

        else :

            while len(self.stack1)!=1 :
                self.stack2.append(self.stack1.pop())

            r=self.stack1[-1]

            while len(self.stack2)!=0 :
                self.stack1.append(self.stack2.pop())


        return r




    def empty(self):
        """
        :rtype: bool
        """

        return len(self.stack1)==0 and len(self.stack2)==0
