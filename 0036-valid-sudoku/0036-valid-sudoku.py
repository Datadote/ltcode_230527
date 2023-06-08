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
                if v in dr[row]:
                    return False
                else:
                    dr[row].append(v)
                if v in dc[col]:
                    return False
                else:
                    dc[col].append(v)
                if v in db[(row//3, col//3)]:
                    return False
                else:
                    db[(row//3, col//3)].append(v)
        return True