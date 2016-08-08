/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root)
    {
        if(root==NULL)
          return true;
    TreeNode *right_mirror=getMirrorImage(root->right);
    return compare(root->left,right_mirror);
    }

    TreeNode* getMirrorImage(TreeNode *root)
    {
    if(root==NULL)
      return NULL;
    TreeNode *left=root->left;
    TreeNode *right=root->right;
    root->left=getMirrorImage(right);
    root->right=getMirrorImage(left);
    return root;




    }

    bool compare(TreeNode *l,TreeNode *r)
    {
        if(l==NULL && r==NULL)
        return true;
        if(l==NULL || r==NULL)
           return false;
        if(l->val!=r->val)
           return false;
        return compare(l->left,r->left) && compare(l->right,r->right);
    }


};
