import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = []
        busy = []

        # Initially, all servers are available
        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))

        ans = []
        time = 0

        for j, task in enumerate(tasks):
            # Task j arrives at second j
            time = max(time, j)

            # Move all servers that have finished into available
            while busy and busy[0][0] <= time:
                finish, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            # If no server is free, wait for the earliest server
            if not available:
                time = busy[0][0]

                # Release every server finishing at this time
                while busy and busy[0][0] <= time:
                    finish, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            # Select the server with minimum weight and index
            weight, idx = heapq.heappop(available)

            ans.append(idx)

            # Server becomes free after this task finishes
            finish_time = time + task
            heapq.heappush(busy, (finish_time, weight, idx))

        return ans