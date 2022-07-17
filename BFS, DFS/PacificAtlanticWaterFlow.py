# depth first search 
# use set to find intersection
# O(rows * columns)

class Solution:
    def pacificAtlantic(self, heights):
        rows = len(heights)
        columns = len(heights[0])
        fromAtlantic = set()
        fromPacific = set()

        def helper(row, column, previous, ocean):
            # if out of range or visited or smaller than neighboring 
            if row < 0 or column < 0 or row > rows - 1 or column > columns - 1 or previous > heights[row][column] or (row, column) in ocean:
                return 
            ocean.add((row, column))
            helper(row + 1, column, heights[row][column], ocean)
            helper(row - 1, column, heights[row][column], ocean)
            helper(row, column - 1, heights[row][column], ocean)
            helper(row, column + 1, heights[row][column], ocean)

        for c in range(columns):
            helper(0, c, 0, fromPacific)
            helper(rows - 1, c, 0, fromAtlantic)
        for r in range(rows):
            helper(r, 0, 0, fromPacific)
            helper(r, columns - 1, 0, fromAtlantic)
        return fromPacific & fromAtlantic

