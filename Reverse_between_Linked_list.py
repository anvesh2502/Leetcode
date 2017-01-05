# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def reverse(self,curr) :

        if curr==None : return None
        if curr.next==None : return curr

        prev=None

        while curr!=None :
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next

        return prev





    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n : return head

        if head==None : return head

        if head.next==None : return head

        if head.next.next==None :
            return self.reverse(head)



        l_prev=None
        right=None
        st=None
        end=None
        right=None

        curr=head

        i=1



        while i<=n :

            if i==m-1 :
                l_prev=curr
                st=curr.next

            if i==n :
                end=curr
                right=curr.next

            i+=1
            curr=curr.next


        if l_prev==None :
            st=head

        else :
         l_prev.next=None

        end.next=None

        rev=self.reverse(st)

        if l_prev!=None :
         l_prev.next=end
        else :
            st.next=right
            return end


        st.next=right


        return head




        
