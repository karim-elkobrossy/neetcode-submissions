import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        squares=collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                current_el=board[r][c]
                if current_el=='.':continue
                if (current_el in rows[r] 
                    or current_el in cols[c] 
                    or current_el in squares[(r//3, c//3)]): return False
                rows[r].add(current_el)
                cols[c].add(current_el)
                squares[(r//3,c//3)].add(current_el)
        return True
