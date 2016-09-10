class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 : return False

        x=0
        y=len(matrix[0])-1

        while x>=0 and x<len(matrix) and y>=0 and y<len(matrix[0]) :

            curr=matrix[x][y]

            if target==curr : return True
            if target>curr : x+=1
            if target<curr : y-=1



        return False
