class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = float('inf')

        best = [INF] * (n + 1)

        ans = INF
        left = 0
        curr_sum = 0

        for right in range(n):
            curr_sum += arr[right]
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
            if curr_sum == target:
                length = right - left + 1

                if best[left] != INF:
                    ans = min(ans, length + best[left])

                best[right + 1] = min(best[right], length)
            else:
                best[right + 1] = best[right]

        return -1 if ans == INF else ans