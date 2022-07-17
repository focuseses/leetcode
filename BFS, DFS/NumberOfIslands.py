# depth-first search
# time: O(row * column), space: O(1)
class Solution:
    def numIslands(self, grid):
        if grid == None:
            return 0
        rows = len(grid)
        columns = len(grid[0])
        islands = 0
     
        def helper(grid, row, column):
            if row < 0 or column < 0 or row >= rows or column >= columns or grid[row][column] == "0":
                return 
            grid[row][column] = "0"
            helper(grid, row - 1, column)
            helper(grid, row + 1, column)
            helper(grid, row, column - 1)
            helper(grid, row, column + 1)
            
        for i in range(rows):
            for j in range(columns):
                if (grid[i][j] == "1"):
                    islands += 1
                    helper(grid, i, j)

        return islands
