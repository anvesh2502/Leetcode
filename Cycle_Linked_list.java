/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head)
    {
    if(head==null)
      return false;

    ListNode fptr=head,sptr=head;

    while(sptr!=null && fptr!=null && fptr.next!=null)
    {
        fptr=fptr.next.next;
        sptr=sptr.next;

        if(sptr==fptr)
          return true;
    }
    return false;



    }
}
