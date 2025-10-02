from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        #transpose 
        for i in range(n):
            # to avoid transposing twice i need to make sure that j>i
            for j in range (i+1,n):
                temp = matrix[i][j]
                matrix[i][j] =  matrix[j][i]
                matrix[j][i] = temp
        # reverse 
        for i in range(n):
            matrix[i].reverse()


sus = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
sus.rotate(matrix)