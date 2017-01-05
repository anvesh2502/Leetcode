# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None : return []


        stack=[]
        l=[]

        stack.append(root)

        while len(stack)!=0 :

            top=stack.pop()
            l.append(top.val)

            trav=top

            if trav.right!=None :
                stack.append(trav.right)

            trav=top

            if trav.left!=None :
                stack.append(trav.left)



        return l







        
