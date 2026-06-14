class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Rows check
        for row in board:
            digits_only = [c for c in row if c!='.']
            # Duplicate check
            if len(set(digits_only))!=len(digits_only): return False
        
        board[0][0], [1][0], [2][0]
        for j in range(9):
            digits_only=[]
            for i in range(9):
                current_element = board[i][j]
                if current_element!='.':digits_only.append(current_element)
            # Duplicate check
            if len(set(digits_only))!=len(digits_only): return False
        
        digits_only=[]
        for i in range(3):
            for j in range(3):
                current_element = board[i][j]
                if current_element!='.':digits_only.append(current_element)
            # Duplicate check
        if len(set(digits_only))!=len(digits_only): return False
        return True

