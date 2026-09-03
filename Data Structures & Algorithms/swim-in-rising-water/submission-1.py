class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        minHeap = [(grid[0][0], 0, 0)]

        time = grid[0][0]

        while minHeap:
            elevation, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue
            
            time = max(time, elevation)
            visited.add((r, c))
            if r == n - 1 and c == n - 1:
                return time
            #add adjacent nodes, 4 directions (horizontal and vertical)
            directions = [
                (r + 1, c),
                (r - 1, c),
                (r, c + 1),
                (r, c - 1)
            ]
            for dr, dc in directions:
                if (
                    dr < 0 or dr > n - 1 or
                    dc < 0 or dc > n - 1 or
                    (dr, dc) in visited
                ):
                    continue
                heapq.heappush(minHeap, (grid[dr][dc], dr, dc))
        return time


        '''
        dijkstras
        each cell is a node --> (elevation, (i, j))
        minHeap plus visited set (visited set to not go in cycle)
        stopping point must reach (n - 1, n -1)

        minHeap should give us lowest elevation when popping from heap
        time = max elevation in the most optimal path (optimal path found through dijkstra)
        '''