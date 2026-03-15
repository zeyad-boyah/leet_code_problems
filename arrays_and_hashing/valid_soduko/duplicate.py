from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # make a hash set for each row, column and 3*3 box
        # for the box the hint says that you can you to which box the element belongs to based on 
        # this formula (row / 3) * 3 + (column / 3)
        # the iterate over each element in the board and asign them to the correct set
        # while checking if they exist or not
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                # Identify which box we are in
                # Formula: (row // 3) * 3 + (column // 3)
                box_num = (r // 3) * 3 + (c // 3)

                # check if we've seen this number in this row, col, or box
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[box_num]):
                    return False

                # Add the number to our sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_num].add(val)

        return True
        
        


test = Solution()
board =[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
test.isValidSudoku(board=board)