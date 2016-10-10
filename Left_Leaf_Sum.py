# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    

    def sumOfLeft(self,root,isLeft) :
        
        if root==None : return 0
        
        if root.left==None and root.right==None and isLeft :
            return root.val
        
        l=self.sumOfLeft(root.left,True)
        r=self.sumOfLeft(root.right,False)
        
        return l+r
        
        
    
    
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None : return 0
        
        if root.left==None and root.right==None : return 0
        
        
        return self.sumOfLeft(root,False)
        

        