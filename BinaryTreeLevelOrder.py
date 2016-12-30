# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self) :

        self.levelMap=dict()

    def createLevelMap(self,root,level=0) :

        if root==None :
            return

        self.levelMap.setdefault(level,[])
        self.levelMap[level].append(root.val)

        self.createLevelMap(root.left,level+1)
        self.createLevelMap(root.right,level+1)




    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.createLevelMap(root,0)


        l=[]
        i=0
        while True :

            if i not in self.levelMap :
                return l
            l.append(self.levelMap[i])
            i+=1

        self.levelMap=dict()





        
