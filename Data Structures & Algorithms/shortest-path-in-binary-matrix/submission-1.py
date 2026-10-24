class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        if len(grid) < 0 or len(grid[0]) < 0 or len(grid) > 100 or len(grid[0]) > 100:
            return -1
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        DIRS = [(0,-1),(0,1),(-1,0),(1,0),
                (-1,-1),(-1,1),(1,-1),(1,1)]
        q = deque([(0, 0, 1)]) # (r, c, dist)
        visited = set()
        visited.add((0,0))
        while q:
            r, c, d = q.popleft()
            if r == len(grid) - 1 and c == len(grid) - 1:
                return d
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid) and (nr, nc) not in visited and grid[nr][nc] == 0:
                    visited.add((nr, nc))
                    q.append((nr, nc, d + 1))
        return -1