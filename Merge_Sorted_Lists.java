/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2)
    {
    int i=0;
    ListNode h=null,prev=null;

    if(l1==null)
      return l2;

    if(l2==null)
      return l1;



    while(l1!=null && l2!=null)
    {
        ListNode node;
        if(l1.val>l2.val)
        {
            node=new ListNode(l2.val);
            l2=l2.next;
        }
        else
        {
            node=new ListNode(l1.val);
            l1=l1.next;
        }

        if(h==null)
          h=node;

        if(prev!=null)
          prev.next=node;

        prev=node;
    }

    ListNode ln=h;
    if(l1!=null)
    {
        while(ln.next!=null)
        {
            ln=ln.next;
        }
        ln.next=l1;
    }
    else if(l2!=null)
    {
        while(ln.next!=null)
        {
            ln=ln.next;
        }
        ln.next=l2;
    }

    return h;
    }
}
