class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(row):
            start, end = 0, len(row)-1
            while start<=end:
                mid=(start+end)//2
                print(start, end, mid)
                if row[mid]==target: return True
                elif row[mid]<target: start+=1
                else: end-=1 
            return False
        found=False
        for row in matrix:
            if target>row[len(row)-1]:continue
            found = binary_search(row)
            if found: return found
        return found      