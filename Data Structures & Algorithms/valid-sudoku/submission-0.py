class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_dict = {}



        for i, row in enumerate(board):
            seen = set()
            for j, val in enumerate(row):
                if val == '.':
                    continue
                if val in seen:
                    return False
                seen.add(val)
            
        for i in range(9):
            seen = set()
            for j, row in enumerate(board):
                if row[i] == '.':
                    continue
                if row[i] in seen:
                    return False
                seen.add(row[i])
        
        
        for sq in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (sq//3) * 3 + i
                    col = (sq%3) *3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])


        return True