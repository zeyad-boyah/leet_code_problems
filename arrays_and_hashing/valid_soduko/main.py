from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_dict = {}
        list_of_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
        for row_index, row in enumerate(board):
            for column_index, column in enumerate(row):
                board_dict[f"{row_index},{column_index}"] = column

        # check rows
        for row_index in range(9):
            # reset the nums_array every row
            temp_list_of_nums = list_of_nums.copy()
            for column_index in range(9):
                if board_dict[f"{row_index},{column_index}"] in temp_list_of_nums:
                    if board_dict[f"{row_index},{column_index}"] == ".":
                        continue
                    else:
                        index = temp_list_of_nums.index(
                            board_dict[f"{row_index},{column_index}"]
                        )
                        temp_list_of_nums[index] = "."
                else:
                    return False

        # check column
        for column_index in range(9):
            # reset the nums_array every column
            temp_list_of_nums = list_of_nums.copy()
            for row_index in range(9):
                if board_dict[f"{row_index},{column_index}"] in temp_list_of_nums:
                    if board_dict[f"{row_index},{column_index}"] == ".":
                        continue
                    else:
                        index = temp_list_of_nums.index(
                            board_dict[f"{row_index},{column_index}"]
                        )
                        temp_list_of_nums[index] = "."
                else:
                    return False

        # check every squared matrix 3x3
        row_start, row_stop = 0, 3
        column_start, column_stop = 0, 3
        while row_start < 9:
            temp_list_of_nums = list_of_nums.copy()
            for row_index in range(row_start, row_stop):
                for column_index in range(column_start, column_stop):
                    if board_dict[f"{row_index},{column_index}"] in temp_list_of_nums:
                        if board_dict[f"{row_index},{column_index}"] == ".":
                            continue
                        else:
                            index = temp_list_of_nums.index(
                                board_dict[f"{row_index},{column_index}"]
                            )
                            temp_list_of_nums[index] = "."
                    else:
                        return False
            column_start += 3
            column_stop += 3
            if column_start == 9:  # end of the 3x3 row
                column_start, column_stop = 0, 3
                row_start += 3
                row_stop += 3
        return True


# neet code solution:
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         cols = defaultdict(set)
#         rows = defaultdict(set)
#         squares = defaultdict(set)  

#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == ".":
#                     continue
#                 if ( board[r][c] in rows[r]
#                     or board[r][c] in cols[c]
#                     or board[r][c] in squares[(r // 3, c // 3)]):
#                     return False

#                 cols[c].add(board[r][c])
#                 rows[r].add(board[r][c])
#                 squares[(r // 3, c // 3)].add(board[r][c])

#         return True



# board = [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# board = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# board=[[".",".",".",".","5",".",".","1","."],
#         [".","4",".","3",".",".",".",".","."],
#         [".",".",".",".",".","3",".",".","1"],
#         ["8",".",".",".",".",".",".","2","."],
#         [".",".","2",".","7",".",".",".","."],
#         [".","1","5",".",".",".",".",".","."],
#         [".",".",".",".",".","2",".",".","."],
#         [".","2",".","9",".",".",".",".","."],
#         [".",".","4",".",".",".",".",".","."]]

# board_dict = {}
# list_of_nums = ['1','2','3','4','5','6','7','8','9',"."]
# for row_index, row in enumerate(board):
#     for column_index, column in enumerate(row):
#         board_dict[f"{row_index},{column_index}"]= column


# # check rows
# for row_index in range(9):
#     # reset the nums_array every row
#     temp_list_of_nums = list_of_nums.copy()
#     for column_index in range(9):
#         if board_dict[f"{row_index},{column_index}"] in temp_list_of_nums:
#             if board_dict[f"{row_index},{column_index}"] == ".":
#                 continue
#             else:
#                 index = temp_list_of_nums.index(board_dict[f"{row_index},{column_index}"])
#                 temp_list_of_nums[index] = "."
#         else:
#             print('false')

# # check column
# for column_index in range(9):
#     # reset the nums_array every column
#     temp_list_of_nums = list_of_nums.copy()
#     for row_index in range(9):
#         if board_dict[f"{row_index},{column_index}"] in temp_list_of_nums:
#             if board_dict[f"{row_index},{column_index}"] == ".":
#                 continue
#             else:
#                 index = temp_list_of_nums.index(board_dict[f"{row_index},{column_index}"])
#                 temp_list_of_nums[index] = "."
#         else:
#             print('false')

# # check every squared matrix 3x3
# row_start, row_stop = 0,3
# column_start, column_stop = 0,3

# while row_start<9:
#     temp_list_of_nums = list_of_nums.copy()
#     for row_index in range(row_start,row_stop):
#         for column_index in range(column_start,column_stop):
#             if board_dict[f"{row_index},{column_index}"] in temp_list_of_nums:
#                 if board_dict[f"{row_index},{column_index}"] == ".":
#                     continue
#                 else:
#                     index = temp_list_of_nums.index(board_dict[f"{row_index},{column_index}"])
#                     temp_list_of_nums[index] = "."
#             else:
#                 print('false')
#     column_start +=3
#     column_stop +=3
#     if column_start == 9: # end of the 3x3 row
#         column_start, column_stop = 0,3
#         row_start +=3
#         row_stop +=3
# print('True')
