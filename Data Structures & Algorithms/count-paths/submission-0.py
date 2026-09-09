class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 1

        cache = [[0] * n for _ in range(m)]

        cache[m - 1][n - 1] = 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1 , -1):
                rightColumn, downRow = c + 1, r + 1
                if 0 <= rightColumn < n:
                    cache[r][c] += cache[r][rightColumn]
                if 0 <= downRow < m:
                    cache[r][c] += cache[downRow][c]
        
        
        return cache[0][0]

        '''
        able to move down or right
            - if move down, cannot move go back to previous row
            - if move right, cannot go back to previous column (left columns)
        
        cache[r][c]
            - compute for every single square
        
        result = sum of right + down

        base case (bottom up)
        Finish cell is 1
        
        define every out of bounds "cell" 0
        compute from down cell and right cell
        '''