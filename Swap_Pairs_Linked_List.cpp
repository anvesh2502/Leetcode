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
    ListNode* swapPairs(ListNode* head)
    {
    if(head==NULL)
       return NULL;

    ListNode *f=head;
    ListNode *s=head->next;


    if(s==NULL)
    {
        return f;
    }

    ListNode *next=s->next;

    s->next=f;
    f->next=swapPairs(next);

    return s;






    }
};
