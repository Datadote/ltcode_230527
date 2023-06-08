class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        dr = defaultdict(list)
        dc = defaultdict(list)
        db = defaultdict(list)
        for row in range(ROWS):
            for col in range(COLS):
                v = board[row][col]
                if v == '.':
                    continue
                if v in dr[row] or v in dc[col] or v in db[(row//3, col//3)]:
                    return False
                dr[row].append(v)
                dc[col].append(v)
                db[(row//3, col//3)].append(v)
        return True