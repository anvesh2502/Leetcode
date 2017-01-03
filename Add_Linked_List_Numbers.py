# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):


    def size(self,l) :

        trav=l
        i=0
        while trav!=None :
            i+=1
            trav=trav.next

        return i




    def add(self,l1,l2) :

        carry=0
        total=0


        l=None


        if l1.next==None :

           total=l1.val+l2.val


           if total>9 :
            carry=1
            total=total%10

           l=ListNode(total)

        else :
            next=self.add(l1.next,l2.next)

            total=l1.val+l2.val+next[1]



            if total>9 :
                carry=1
                total%=10

            l=ListNode(total)
            l.next=next[0]

        return (l,carry)
















    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None and l2==None : return None

        s1=self.size(l1)
        s2=self.size(l2)

        diff=s1-s2

        if diff<0 :

            d=abs(diff)
            i=0

            while i<d :

                n=ListNode(0)
                n.next=l1
                l1=n
                i+=1

        elif diff>0 :

            d=abs(diff)
            i=0

            while i<d :
                n=ListNode(0)
                n.next=l2
                l2=n
                i+=1


        ret=self.add(l1,l2)


        if ret[1]==1 :

            new_head=ListNode(1)
            new_head.next=ret[0]
            return new_head

        return ret[0]














            
