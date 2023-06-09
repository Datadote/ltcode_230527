class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        COLS, ROWS = len(matrix[0]), len(matrix)
        L, R = 0, ROWS-1
        while L <= R:
            M = L + (R-L)//2
            if target > matrix[M][-1]:
                L = M + 1
            elif target < matrix[M][0]:
                R = M - 1
            else:
                break
        row = M
        L, R = 0, COLS-1
        while L <= R:
            M = L + (R-L)//2
            if target > matrix[row][M]:
                L = M + 1
            elif target < matrix[row][M]:
                R = M - 1
            else:
                return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # L, R = 0, len(matrix)-1
        # while L <= R:
        #     M = L + (R-L)//2
        #     if target > matrix[M][-1]:
        #         L = M + 1
        #     elif target < matrix[M][0]:
        #         R = M - 1
        #     else:
        #         break
        # row = M
        # L, R = 0, len(matrix[0])-1
        # while L <= R:
        #     M = L + (R-L)//2
        #     if target > matrix[row][M]:
        #         L = M + 1
        #     elif target < matrix[row][M]:
        #         R = M - 1
        #     else:
        #         return True
        # return False
        
        # L, R = 0, len(matrix) - 1
        # while L <= R:
        #     M = L + (R-L)//2
        #     if target > matrix[M][-1]:
        #         L = M + 1
        #     elif target < matrix[M][0]:
        #         R = M - 1
        #     else:
        #         break
        # row = M
        # L, R = 0, len(matrix[0])-1
        # while L <= R:
        #     M = L + (R-L)//2
        #     if target > matrix[row][M]:
        #         L = M + 1
        #     elif target < matrix[row][M]:
        #         R = M - 1
        #     else:
        #         return True
        # return False
        
        # L, R = 0, len(matrix)-1
        # while L <= R:
        #     M = L + (R-L)//2
        #     if target > matrix[M][-1]:
        #         L = M + 1
        #     elif target < matrix[M][0]:
        #         R = M - 1
        #     else:
        #         break
        # row = M
        # L, R = 0, len(matrix[0])-1
        # while L <= R:
        #     M = L + (R-L)//2
        #     if target > matrix[row][M]:
        #         L = M + 1
        #     elif target < matrix[row][M]:
        #         R = M - 1
        #     else:
        #         return True
        # return False
        
        # L, R = 0, len(matrix)-1
        # while L <= R:
        #     M = L + (R-L)//2
        #     if target > matrix[M][-1]:
        #         L = M + 1
        #     elif target < matrix[M][0]:
        #         R = M - 1
        #     else:
        #         break
        # row = M
        # L, R = 0, len(matrix[0])-1
        # while L <= R:
        #     M = L + (R-L)//2
        #     if target > matrix[row][M]:
        #         L = M + 1
        #     elif target < matrix[row][M]:
        #         R = M - 1
        #     elif target == matrix[row][M]:
        #         return True
        # return False
        
        # L, R = 0, len(matrix)-1
        # while L <= R:
        #     M = L + (R-L)//2
        #     if target > matrix[M][-1]:
        #         L = M + 1
        #     elif target < matrix[M][0]:
        #         R = M - 1
        #     else:
        #         break
        # row = M
        # L, R = 0, len(matrix[row])-1
        # while L <= R:
        #     M = L + (R-L)//2
        #     if target == matrix[row][M]:
        #         return True
        #     elif target > matrix[row][M]:
        #         L = M + 1
        #     else:
        #         R = M - 1
        # return False