/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseKGroup(ListNode head, int k)
    {
    int count=0;
    ListNode trav=head;
    while(trav!=null)
    {
        trav=trav.next;
        count++;
    }

    if(count<k)
       return head;

    ListNode curr=head,prev=null,next=null;
    int i=0;
    while(i<k)
    {
        next=curr.next;
        curr.next=prev;
        prev=curr;
        curr=next;
        i++;
    }

    trav=prev;
    while(trav.next!=null)
      trav=trav.next;
    trav.next=reverseKGroup(next,k);

    return prev;


    }
}
