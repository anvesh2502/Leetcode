# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None : return None
        if head.next==None : return head
        if k==0 : return head


        length=0
        trav=head



        while trav!=None :
            trav=trav.next
            length+=1

        k%=length


        index=length-k-1

        i=0
        trav=head

        while i<index :
            trav=trav.next
            i+=1

        if trav==None : return head

        rev=trav.next
        trav.next=None

        trav=rev

        if trav==None : return head

        while trav.next!=None :
            trav=trav.next

        trav.next=head


        return rev








            
