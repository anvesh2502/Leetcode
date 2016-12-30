class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1=[]
        self.queue2=[]


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.empty() :
            self.queue1.append(x)
            return

        if len(self.queue1)==0 :
            self.queue2.append(x)
        else :
            self.queue1.append(x)




    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty() :
            return

        if len(self.queue1)==0 :

            for i in range(0,len(self.queue2)-1) :
                self.queue1.append(self.queue2[i])

            self.queue2.pop()
            self.queue2=[]

        else :

            for i in range(0,len(self.queue1)-1) :
                self.queue2.append(self.queue1[i])

            self.queue1.pop()
            self.queue1=[]





    def top(self):
        """
        :rtype: int
        """
        if self.empty() : return None

        r=-1

        if len(self.queue1)==0 :

            for i in range(0,len(self.queue2)-1) :
                self.queue1.append(self.queue2[i])

            r=self.queue2.pop()
            self.queue2=[]
            self.queue1.append(r)

        else :

            for i in range(0,len(self.queue1)-1) :
                self.queue2.append(self.queue1[i])

            r=self.queue1.pop()
            self.queue1=[]
            self.queue2.append(r)

        return r






    def empty(self):
        """
        :rtype: bool
        """

        return len(self.queue1)==0 and len(self.queue2)==0


st=Stack()
st.push(1)
st.push(2)
st.push(3)
print st.top()
print st.top()
st.pop()
print st.top()
