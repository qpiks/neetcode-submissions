class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        box = {}
        for i in board:
            for j in i:
                if j != "." and row.get(j):
                    return False
                row.update({j: 1})
            row = {}
        for i in range(9):
            for j in range(9):
                print(col)
                if board[j][i] != "." and col.get(board[j][i]):
                    return False
                col.update({board[j][i]: 1})
            col = {}
        crow = ccol = 0;
        for i in range(9):
            for j in range(3):
                for k in range(3):
                    if board[j + 3*crow][k + 3*ccol] != "." and box.get(board[j + 3*crow][k + 3*ccol]):
                        return False
                    box.update({board[j + 3*crow][k + 3*ccol]: 1})
            box = {}
            crow = i // 3
            ccol = i % 3
        return True






        