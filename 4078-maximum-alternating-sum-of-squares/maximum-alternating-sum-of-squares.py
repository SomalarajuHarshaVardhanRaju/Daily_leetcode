
class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        squares = sorted(num * num for num in nums)

        n = len(squares)
        positive_count = (n + 1) // 2

        return sum(squares[n - positive_count:]) - sum(squares[:n - positive_count])
