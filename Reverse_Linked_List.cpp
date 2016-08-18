/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head)
    {
      return reverseList(head,NULL);
    }

    ListNode* reverseList(ListNode* curr,ListNode *prev)
    {

      if(curr==NULL)
         return prev;
      ListNode* next=curr->next;
      curr->next=prev;
      return reverseList(next,curr);

    }


};
