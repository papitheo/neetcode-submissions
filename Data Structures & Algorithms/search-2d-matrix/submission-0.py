class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_rows, len_col = len(matrix),len(matrix[0])

        left_ptr,right_ptr = 0, (len_rows * len_col) - 1

        while left_ptr <= right_ptr:
            mid_index = left_ptr + (right_ptr - left_ptr) // 2

            row_ptr = mid_index // len_col
            col_ptr = mid_index % len_col

            if target == matrix[row_ptr][col_ptr]:
                return True
            elif target < matrix[row_ptr][col_ptr]:
                right_ptr = mid_index - 1
            else:
                left_ptr =  mid_index + 1
        
        return False
                