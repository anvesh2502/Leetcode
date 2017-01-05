# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):


    def merge(self,l1,l2) :

        if l1==None and l2==None :
            return None

        if l1==None :
            return l2

        if l2==None :
            return l1

        new_head=None
        tail=None

        while l1!=None and l2!=None :

            next1=l1.next
            next2=l2.next


            if l1.val>l2.val :

                l2.next=None
                if new_head==None :
                    new_head=l2
                    tail=l2

                else :
                    tail.next=l2
                    tail=l2

                l2=next2

            else :

                l1.next=None
                if new_head==None :
                    new_head=l1
                    tail=l1

                else :
                    tail.next=l1
                    tail=l1

                l1=next1

        if l1==None and l2==None :
            return new_head

        if l1==None :
            tail.next=l2

        if l2==None :
            tail.next=l1

        return new_head














    def merge_sort(self,head) :

        if head==None or head.next==None :
            return head

        fptr=head
        sptr=head

        while fptr!=None and fptr.next!=None :
            fptr=fptr.next.next
            prev=sptr
            sptr=sptr.next

        prev.next=None

        l1=self.merge_sort(head)
        l2=self.merge_sort(sptr)


        return self.merge(l1,l2)














    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        return self.merge_sort(head)


        
