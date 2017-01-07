# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


    def insertNode(self,root,node) :

        if root==None :
            return

        if root.val>node.val :

            if root.left==None :
                root.left=node
                return

            self.insertNode(root.left,node)
            return

        if root.val<node.val :

            if root.right==None :
                root.right=node
                return

            self.insertNode(root.right,node)
            return




    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        if root==None : return None


        if root.val==key :

            if root.left==None and root.right==None : return None

            if root.left==None :
                return root.right

            if root.right==None :
                return root.left

            left=root.left
            right=root.right

            if left.val>right.val :
                self.insertNode(left,right)
                return left

            self.insertNode(right,left)
            return right

        else :

            if root.val>key :
                root.left=self.deleteNode(root.left,key)

            else :
                root.right=self.deleteNode(root.right,key)


            return root
















        
