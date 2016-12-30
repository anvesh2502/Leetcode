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
        if self.empty() :
            self.stack1.append(x)
            return

        if len(self.stack1)==0 :
            self.stack2.append(x)

        else :
            self.stack1.append(x)





    def pop(self):
        """
        :rtype: nothing
        """

        if self.empty() :
            return

        if len(self.stack1)==0 :

            while len(self.stack2)!=1 :
                self.stack1.append(self.stack2.pop())

            self.stack2.pop()

        else :

            while len(self.stack1)!=1 :
                self.stack2.append(self.stack1.pop())

            self.stack1.pop()







    def peek(self):
        """
        :rtype: int
        """
        if self.empty() :
            return None

        r=0

        if len(self.stack1)==0 :

            while len(self.stack2)!=1 :
                self.stack1.append(self.stack2.pop())

            r=self.stack2.pop()
            self.stack1.append(r)

        else :

            while len(self.stack1)!=1 :
                self.stack2.append(self.stack1.pop())

            r=self.stack1.pop()
            self.stack2.append(r)


        return r




    def empty(self):
        """
        :rtype: bool
        """

        return len(self.stack1)==0 and len(self.stack2)==0





queue=Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
print queue.peek()
queue.pop()
print queue.peek()
