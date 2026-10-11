class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        size = len(matrix) * len(matrix[0])
        l, r = 0, size - 1
        while l <= r:
            m = l + ((r - l) // 2)
            row = int(m // len(matrix[0]))
            col = int(m % len (matrix[0]))
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                l = l + 1
            else:
                r = r - 1
        return False

        
