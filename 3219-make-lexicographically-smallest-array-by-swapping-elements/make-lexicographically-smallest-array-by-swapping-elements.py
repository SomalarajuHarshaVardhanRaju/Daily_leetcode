from typing import List
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = sorted((nums[i], i) for i in range(n))
        ans = [0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1
            indices = []
            for k in range(i, j + 1):
                indices.append(arr[k][1])
            indices.sort()
            for k, idx in enumerate(indices):
                ans[idx] = arr[i + k][0]
            i = j + 1
        return ans