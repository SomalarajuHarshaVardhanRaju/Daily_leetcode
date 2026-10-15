
class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0

        for i in range(n):
            seen = set()

            for j in range(i, n):
                seen.add(nums[j])

                distinct = len(seen)
                total += distinct * distinct

        return total
