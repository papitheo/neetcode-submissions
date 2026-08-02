from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Declare the 9x9 matrix and sub-box
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        sub_box = [set() for _ in range(9)]
        
        # iterate through the given board for val
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                box_index = (r // 3) * 3 + (c // 3)
                
                if (val in row[r]) or (val in col[c]) or (val in sub_box[box_index]):
                    return False

                row[r].add(val)
                col[c].add(val)
                sub_box[box_index].add(val)

        return True