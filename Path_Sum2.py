# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


    def get_path_lists(self,root) :

        if root==None :
            return []

        if root.left==None and root.right==None :
            return [[root.val]]

        left=self.get_path_lists(root.left)
        right=self.get_path_lists(root.right)

        result_lists=[]

        for l in left :
            result_lists.append([root.val]+l)

        for l in right :
            result_lists.append([root.val]+l)

        return result_lists






    def pathSum(self, root, total):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        if root==None :
            return []


        if root.left==None and root.right==None :

            if total==root.val :
             return [[root.val]]
            return []


        result=[]



        all_lists=self.get_path_lists(root.left)+self.get_path_lists(root.right)
        val=root.val

        for l in all_lists :

            if (sum(l)+val)==total :
                result.append([val]+l)


        return result










        
