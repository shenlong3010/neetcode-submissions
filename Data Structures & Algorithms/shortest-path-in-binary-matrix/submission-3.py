class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        if len(grid) < 0 or len(grid[0]) < 0 or len(grid) > 100 or len(grid[0]) > 100:
            return -1
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        n = len(grid)
        DIRS = [(0,-1),(0,1),(-1,0),(1,0),
                (-1,-1),(-1,1),(1,-1),(1,1)]
        q = deque([(0, 0, 1)]) # (r, c, dist)
        grid[0][0] = 1
        while q:
            r, c, d = q.popleft()
            if r == n - 1 and c == n - 1:
                return d
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    q.append((nr, nc, d + 1))
        return -1