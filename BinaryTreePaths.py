# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}

    def __init__(self) :

        self.paths=[]

    def get_paths(self,root,path='') :

        if root==None :
            return

        if root.left==None and root.right==None :
            path+=str(root.val)
            self.paths.append(path)
            return

        path+=str(root.val)+'->'

        self.get_paths(root.left,path)
        self.get_paths(root.right,path)







    def binaryTreePaths(self, root):

        self.get_paths(root,'')
        return self.paths



        
