class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            set_row = set()
            set_col = set()
            for j in range(9):
                # check row
                if board[i][j] != '.':
                    if board[i][j] in set_row:
                        return False
                    set_row.add(board[i][j])

                # check col
                if board[j][i] != '.':
                    if board[j][i] in set_col:
                        return False
                    set_col.add(board[j][i])
        
        for k in range(1, 10):
            set_box = set()
            for i in range(9):
                for j in range(9):
                    if (i // 3 + 1) + 3 * (j // 3) == k:
                        if board[i][j] != ".":
                            if board[i][j] in set_box:
                                return False
                            set_box.add(board[i][j])

        return True
