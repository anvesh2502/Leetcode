/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeElements(ListNode head, int val)
    {
        ListNode trav=head;
        if(trav==null)
          return trav;
        while(trav!=null && trav.next!=null)
        {
            if(trav.next.val==val)
            {
                trav.next=trav.next.next;
            }
            else
              trav=trav.next;
        }

        if(head.val==val)
          head=head.next;
        return head;


    }
}
