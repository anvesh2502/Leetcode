# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
          self.val = x
          self.next = None


class Solution(object):


    def reverse(self,curr,prev=None) :

        if curr==None : return prev


        next=curr.next
        curr.next=prev
        return self.reverse(next,curr)







    def partition(self, head, x):

        if head==None : return None

        if head.next==None : return head

        prev=None
        curr=head
        less=None

        while curr!=None :

            if curr.val>=x :

                next=curr.next

                if prev==None :
                    curr.next=less
                    less=curr
                    curr=next
                    head=curr

                else :
                    prev.next=next
                    curr.next=less
                    less=curr
                    curr=next

            else :

                prev=curr
                curr=curr.next


        if less==None : return head

        less=self.reverse(less)

        if head==None : return less



        trav=head


        while trav.next!=None :
            trav=trav.next

        trav.next=less

        return head
