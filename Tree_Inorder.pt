# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]

        visited=set()

        if root==None : return []

        stack.append(root)

        l=[]

        while len(stack)!=0 :

            top=stack[-1]

            if top.left==None  :
                l.append(top.val)
                visited.add(top)
                stack.pop()

                if top.right!=None :
                    stack.append(top.right)


            else :

                if top.left in visited :
                    l.append(top.val)
                    visited.add(top)
                    stack.pop()
                    if top.right!=None :
                     stack.append(top.right)

                else :

                    trav=top

                    while trav.left!=None :
                     stack.append(trav.left)
                     trav=trav.left




        return l






















        
