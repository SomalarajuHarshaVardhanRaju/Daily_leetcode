from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i, value):
        while i <= self.n:
            self.tree[i] += value
            i += i & -i

    def query(self, i):
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & -i
        return result

    # Find the smallest index whose prefix sum >= k
    def kth(self, k):
        idx = 0
        bit = 1 << (self.n.bit_length() - 1)

        while bit:
            nxt = idx + bit

            if nxt <= self.n and self.tree[nxt] < k:
                idx = nxt
                k -= self.tree[nxt]

            bit >>= 1

        return idx + 1


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        # Coordinate compression
        values = sorted(set(nums))
        m = len(values)

        counts = Fenwick(m)
        sums = Fenwick(m)

        # Calculate the cost of every window of size x
        costs = []
        total_sum = 0

        for i in range(n):
            idx = bisect_left(values, nums[i]) + 1

            counts.add(idx, 1)
            sums.add(idx, nums[i])
            total_sum += nums[i]

            # Remove the element outside the window
            if i >= x:
                old = nums[i - x]
                old_idx = bisect_left(values, old) + 1

                counts.add(old_idx, -1)
                sums.add(old_idx, -old)
                total_sum -= old

            if i >= x - 1:
                # Find the median
                median_idx = counts.kth((x + 1) // 2)
                median = values[median_idx - 1]

                # Count and sum of elements smaller than median
                left_count = counts.query(median_idx - 1)
                left_sum = sums.query(median_idx - 1)

                # Elements equal to or greater than median
                right_count = x - left_count
                right_sum = total_sum - left_sum

                # Minimum cost to make this window equal
                cost = (
                    median * left_count - left_sum
                    + right_sum - median * right_count
                )

                costs.append(cost)

        # DP: choose exactly j non-overlapping windows
        INF = float('inf')

        # Zero windows have zero cost for every prefix
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                # Option 1: Skip the current element
                curr[i] = curr[i - 1]

                # Option 2: Choose a window ending at i - 1
                if i >= x:
                    candidate = prev[i - x] + costs[i - x]
                    curr[i] = min(curr[i], candidate)

            prev = curr

        return prev[n]