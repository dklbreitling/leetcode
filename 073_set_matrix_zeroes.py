class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        for r in range(n_rows):
            for c in range(n_cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
        for r in range(n_rows):
            for c in range(n_cols):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0
