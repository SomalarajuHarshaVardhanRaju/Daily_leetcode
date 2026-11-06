
class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda log: log[1])

        # Store queries with their original indices
        sorted_queries = sorted(
            (q, i) for i, q in enumerate(queries)
        )

        ans = [0] * len(queries)

        # Number of requests for each server in current window
        count = [0] * (n + 1)

        active = 0
        left = 0
        right = 0

        for q, idx in sorted_queries:
            start = q - x

            # Add requests with time <= q
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]

                if count[server] == 0:
                    active += 1

                count[server] += 1
                right += 1

            # Remove requests with time < q - x
            while left < right and logs[left][1] < start:
                server = logs[left][0]

                count[server] -= 1

                if count[server] == 0:
                    active -= 1

                left += 1

            # Total servers - active servers
            ans[idx] = n - active

        return ans
