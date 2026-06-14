class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """The trick in this question is that we want a solution in O(log(m * n)). Since O(log(n)) is the binary search time complexity, then in order to make it in a time complexity log(m*n), we need to apply binary search on a flattened matrix (1D). We could flatten this matrix and the entire matrix would be in ascending order. If we want to flatten it, it would take us O(M*N) which is worse than log(m*n). We could treat it as a single row by making the start and end equal 0, (m*n)-1 and calculate the col and row of the element we want to search for (mid element) """
        self.m = len(matrix)
        self.n = len(matrix[0])
        # start and end are 0 and length of the entire matrix-1
        start, end = 0, (self.m*self.n)-1

        # Retrieves the row and column of the mid element based on the index
        def calc_row_col(index):
            row = int(index/self.n) 
            col = index%self.n
            print(index, row, col)
            return row, col

        while start<=end:
            mid = (start+end)//2
            mid_coordinates = calc_row_col(mid)
            if matrix[mid_coordinates[0]][mid_coordinates[1]]==target: return True
            elif matrix[mid_coordinates[0]][mid_coordinates[1]] < target: start=mid+1
            else: end=mid-1
        return False