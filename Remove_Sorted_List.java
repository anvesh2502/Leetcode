/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head)
    {
    ListNode trav=head,h=head;
    if(trav==null)
      return null;
    while(trav!=null && trav.next!=null)
    {
        if(trav.val==trav.next.val)
        {
          ListNode next=trav.next.next;
          trav.next=trav.next.next;
        }
        else
        {

            trav=trav.next;
        }
    }

    return h;
    }
}
