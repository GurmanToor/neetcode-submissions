class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        colored = set()
        starting_color = image[sr][sc]

        if image[sr][sc] == color:
            return image

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            colored.add((r, c))
            image[r][c] = color

            while q:
                r,c = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(len(image)) and col in range(len(image[0])) and image[row][col] == starting_color and (row, col) not in colored:
                        image[row][col] = color
                        q.append((row, col))
            return image
        
        return bfs(sr, sc)