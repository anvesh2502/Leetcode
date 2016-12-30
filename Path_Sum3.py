# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


    def treeSum(self,root,sum) :

        if root==None :
            return ([],0)

        if root.left==None and root.right==None :
           if root.val==sum :
               return ([root.val],1)
           return ([root.val],0)

        left=self.treeSum(root.left,sum)
        right=self.treeSum(root.right,sum)

        count=0

        if root.val==sum :
            count+=1

        count+=left[1]+right[1]

        vals=left[0]+right[0]

        for v in vals :
            if (sum-v)==root.val :
                count+=1

        new_vals=[]
        new_vals.append(root.val)

        for v in vals :
            new_vals.append(v+root.val)


        return ([new_vals,count])






    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        res=self.treeSum(root,sum)
        return res[1]







        
