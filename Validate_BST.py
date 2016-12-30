# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


    def __init__(self) :

        self.l=[]


    def getList(self,root) :

        if root!=None :
            self.getList(root.left)
            self.l.append(root.val)
            self.getList(root.right)



    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.getList(root)

        if len(self.l)<=1 : return True


        for i in range(1,len(self.l)) :

            if self.l[i-1]>=self.l[i] : return False

        return True


        
