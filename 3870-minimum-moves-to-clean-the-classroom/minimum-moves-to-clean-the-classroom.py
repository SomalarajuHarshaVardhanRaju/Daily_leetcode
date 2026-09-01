class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        start = None

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i,j)
                elif classroom[i][j] == 'L':
                    litter[(i,j)] = len(litter)
        total_litter = len(litter)

        if total_litter == 0:
            return 0

        queue = deque()
        queue.append((start[0], start[1], energy, 0))

        visited = set()
        visited.add((start[0],start[1],energy,0))

        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
        moves = 0

        while queue:
            size = len(queue)

            for _ in range(size):
                r, c, e, mask = queue.popleft()

                # All litter collected
                if mask == (1 << total_litter) - 1:
                    return moves

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Outside grid
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

    
                    if classroom[nr][nc] == 'X':
                        continue

    
                    if e == 0:
                        continue

                    new_energy = e - 1
                    new_mask = mask

                    if (nr, nc) in litter:
                        idx = litter[(nr, nc)]
                        new_mask |= (1 << idx)

                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    state = (nr, nc, new_energy, new_mask)

                    if state not in visited:
                        visited.add(state)
                        queue.append(state)

            moves += 1

        return -1
