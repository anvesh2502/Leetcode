# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


    def __init__(self) :

      self.level=dict()

    def buildRightTree(self,root,index=0) :

        if root==None : return
        self.level.setdefault(index,[])
        self.level[index].append(root.val)
        self.buildRightTree(root.left,index+1)
        self.buildRightTree(root.right,index+1)







    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l=[]
        self.buildRightTree(root)
        i=0
        while i in self.level :
            l.append(self.level[i][-1])
            i+=1

        return l




        
