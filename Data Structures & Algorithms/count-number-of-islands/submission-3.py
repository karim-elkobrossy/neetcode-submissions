class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0]) 
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        visited_nodes = set((0, 0))
        count=0

        def dfs(i, j):
            for dr, dc in directions:
                neighbor_r, neighbor_c = i+dr, j+dc
                print(neighbor_r, neighbor_c)
                # Check if within boundary first
                if 0 <= neighbor_r < n_rows and 0 <= neighbor_c < n_cols:
                    # Add if water
                    if grid[neighbor_r][neighbor_c] == "1":
                        if (neighbor_r, neighbor_c) in visited_nodes: continue
                        visited_nodes.add((neighbor_r, neighbor_c))
                        dfs(neighbor_r, neighbor_c)


        # If I found an unvisited land, dfs then increment count
        for i in range(n_rows):
            for j in range(n_cols):
                # water present
                if grid[i][j] == "0" or (i, j) in visited_nodes: continue
                # dfs will mark visited nodes to remove duplicate count
                dfs(i, j)
                count+=1
        return count
