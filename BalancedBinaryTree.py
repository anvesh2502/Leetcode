# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


    def get_balance(self,root) :

       if root==None :
           return [0,True]

       if root.left==None and root.right==None :
           return [1,True]

       left=self.get_balance(root.left)
       right=self.get_balance(root.right)
       left[0]+=1
       right[0]+=1

       if abs(left[0]-right[0])>1 :
           return [max(left[0],right[0]),False]

       return [max(left[0],right[0]),left[1] and right[1]]






    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res=self.get_balance(root)
        return res[1]

        
