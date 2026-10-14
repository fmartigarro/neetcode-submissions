class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        grid_sets = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                # combo of i and j, need to convert to one number
                
                grid_index = (i // 3) * 3 + (j // 3)
                
                if board[i][j] in row_sets[i]:
                    return False
                if board[i][j] in col_sets[j]:
                    return False
                if board[i][j] in grid_sets[grid_index]:
                    return False
                
                row_sets[i].add(board[i][j])
                col_sets[j].add(board[i][j])
                grid_sets[grid_index].add(board[i][j])
        
        return True


                
                
    
