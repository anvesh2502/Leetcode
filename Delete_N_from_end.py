# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head==None : return None

        prev=None
        fptr=head
        sptr=head
        i=0

        while fptr.next!=None :

            fptr=fptr.next
            if i<n-1 :
                i+=1
            else :
                prev=sptr
                sptr=sptr.next


        if prev==None :
            head=head.next
        else :
            prev.next=sptr.next


        return head
