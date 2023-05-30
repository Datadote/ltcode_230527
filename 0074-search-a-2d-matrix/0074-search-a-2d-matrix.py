class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix)-1
        while L <= R:
            M = L + (R-L)//2
            if target > matrix[M][-1]:
                L = M + 1
            elif target < matrix[M][0]:
                R = M - 1
            else:
                break
        row = M
        # print(L, R, row)
        # if not (L <= R):
        #     return False
        L, R = 0, len(matrix[row])-1
        while L <= R:
            M = L + (R-L)//2
            if target == matrix[row][M]:
                return True
            elif target > matrix[row][M]:
                L = M + 1
            else:
                R = M - 1
            
        return False