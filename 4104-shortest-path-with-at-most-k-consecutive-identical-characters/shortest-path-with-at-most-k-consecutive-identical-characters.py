import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))

        # dist[node][count] = minimum cost to reach node
        # with count consecutive occurrences of labels[node]
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        # Starting node contributes its label
        dist[0][1] = 0

        pq = [(0, 0, 1)]  # cost, node, consecutive count

        while pq:
            cost, u, count = heapq.heappop(pq)

            if cost != dist[u][count]:
                continue

            if u == n - 1:
                return cost

            for v, w in graph[u]:
                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][new_count]:
                    dist[v][new_count] = new_cost
                    heapq.heappush(pq, (new_cost, v, new_count))

        return -1