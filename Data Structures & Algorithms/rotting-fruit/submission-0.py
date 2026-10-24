class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        minutes = 0
        fresh = 0
        q = collections.deque()

        for i in range(len(grid)):
            for r in range(len(grid[0])):
                if grid[i][r] == 2:
                    q.append((i, r))
                    rotten.add((i, r))
                elif grid[i][r] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(len(grid)) and col in range(len(grid[0])) and (row, col) not in rotten and grid[row][col] == 1:
                        rotten.add((row, col))
                        fresh -= 1
                        q.append((row, col))
            minutes += 1
        if fresh == 0:
            return minutes
        else:
            return -1
