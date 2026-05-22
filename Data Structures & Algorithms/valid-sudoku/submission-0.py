class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        co=defaultdict(set)
        ro=defaultdict(set)
        s=defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] =='.':
                    continue
                if(board[r][c] in ro[r] or board[r][c] in co[c] or board[r][c] in s[(r//3,c//3)]):
                    return False
                co[c].add(board[r][c])
                ro[r].add(board[r][c])
                s[(r//3,c//3)].add(board[r][c])
        return True