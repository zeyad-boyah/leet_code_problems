from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # start by checking start and finish of the middle row if target lies between it 
        # and move the middle row as if doing a binary search
        # then do a binary search on it 
        if not matrix or not matrix[0]:
            return False
        top, bot = 0, len(matrix)-1
        while top <=bot:
            mid = top + ((bot-top)//2)
            if target > matrix[mid][-1]:
                top = mid +1
            elif target < matrix[mid][0]:
                bot = mid -1
            else:
                row = matrix[mid]
                break
        else:
            return False
        l,r = 0, len(row)-1
        
        while l <= r:
            m = l+ ((r-l)//2)
            if row[m] < target:
                l= m +1
            elif row[m]> target:
                r = m-1
            else:
                return True
        return False

test = Solution()
matrix=[[0]]
target=0
# matrix=[[1,2,4,8],[10,11,12,13],[14,20,30,40]]
# target=10
test.searchMatrix(matrix=matrix, target=target)