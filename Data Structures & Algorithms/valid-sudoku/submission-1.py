class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        """
        1. Check row 1-9 for no duplicates
        2. Check column 1-9 no duplicates
        3. Need to check block square 1-9 no duplicates

        Input = [[][][][][][][][][]]
        Output = False/True

        Hashmap/Set to check for duplicates//use set for this

        3 methods (sections)

        1. index-value -- (row/3) * 3 + (col/3)

        #store number / index
        """

        seen = set()
        for i in range(9):
            for j in range(9):
                if not board[i][j].isdigit():
                    continue
                elif (board[i][j], i) in seen:
                    return False
                else:
                    seen.add((board[i][j], i))

        seen = set()
        for j in range(9):
            for i in range(9):
                if not board[i][j].isdigit():
                    continue
                elif (board[i][j], j) in seen:
                    return False
                else:
                    seen.add((board[i][j], j))

        seen = set()
        for i in range(9):
            for j in range(9):
                idx = (i//3, j//3)
                if not board[i][j].isdigit():
                    continue
                elif (board[i][j], idx) in seen:
                    return False
                else:
                    seen.add((board[i][j], idx))

        return True
 
