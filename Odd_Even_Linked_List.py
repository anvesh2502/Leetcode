# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def reverse(self,curr,prev=None) :

        if curr==None :
            return prev

        next=curr.next
        curr.next=prev
        return self.reverse(next,curr)



    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None : return None

        if head.next==None : return head

        curr=head
        prev=None
        even=None
        i=1

        while curr!=None :

            next=curr.next

            if (i%2)==0 :

                if prev==None :
                    curr.next=even
                    even=curr
                    curr=next
                    head=curr
                else :
                    curr.next=even
                    even=curr
                    prev.next=next
                    curr=next

            else :
                prev=curr
                curr=next

            i+=1



        if even==None : return head

        if head==None : return even

        even=self.reverse(even)

        trav=head

        while trav.next!=None :
            trav=trav.next

        trav.next=even


        return head


















        
