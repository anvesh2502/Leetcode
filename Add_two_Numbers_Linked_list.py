# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):


    def reverse(self,curr,prev=None) :
        if curr==None : return prev
        next=curr.next
        curr.next=prev
        return self.reverse(next,curr)







    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None and l2==None : return None
        if l1==None : return l2
        if l2==None : return l1

        count1=0
        count2=0

        trav=l1

        while trav!=None :
            trav=trav.next
            count1+=1

        trav=l2

        while trav!=None :
            trav=trav.next
            count2+=1

        diff=abs(count1-count2)

        if count1>count2 :
            trav=l2
        else :
            trav=l1

        while trav.next!=None :
            trav=trav.next

        i=0
        while i<diff :
            node=ListNode(0)
            trav.next=node
            trav=node
            i+=1
        trav.next=None

        head=None
        carry=0

        while l1!=None :
            result=l1.val+l2.val+carry
            if result>9 and l1.next!=None:

                result%=10
                carry=1
            else :
                carry=0
            node=ListNode(result)
            node.next=head
            head=node
            l1=l1.next
            l2=l2.next

        if head.val>9 :
            head.val=head.val%10
            node=ListNode(1)
            node.next=head
        else :
            node=head

        return self.reverse(node)















        
