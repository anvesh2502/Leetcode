# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):


  def getIntersectionNode(self, a, b):

    if a==None or b==None : return None

    aLength=0
    bLength=0

    trav=a
    while trav!=None :
        trav=trav.next
        aLength+=1

    trav=b
    while trav!=None :
        trav=trav.next
        bLength+=1


    if aLength<bLength :
        temp=b
        b=a
        a=temp
    diff=abs(bLength-aLength)

    i=0
    while a!=None and b!=None :

        if i<diff :
            a=a.next
            i+=1
        else :
            if a==b : return a
            a=a.next
            b=b.next

    return None












        
