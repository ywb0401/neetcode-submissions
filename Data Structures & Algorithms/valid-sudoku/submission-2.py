class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        set3 = set()
        for i in range(9):
            set1 = set()
            set2 = set()
            for j in range(9):
                
                # print(i,j,board[i][j])
                if board[i][j] != ".":
                    if board[i][j] in set1:
                        return False
                    set1.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in set2:
                        return False
                    set2.add(board[j][i])
        
        for k in range(1, 10):
            set3 = set()
            for i in range(9):
                for j in range(9):
                    if i // 3 + 3 * (j // 3) + 1 == k:
                        if board[i][j] != ".":
                            if board[i][j] in set3:
                                return False
                            set3.add(board[i][j])



        return True