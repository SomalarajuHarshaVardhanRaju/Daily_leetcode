
class Solution:
    def minOperations(self, s: str) -> int:
        target = ''.join(sorted(s))

        if s == target:
            return 0

        n = len(s)

        if n == 2:
            return -1

        smallest = min(s)
        largest = max(s)

        # At least one endpoint is already correct
        if s[0] == smallest or s[-1] == largest:
            return 1

        # Both endpoints are the wrong extremes
        if s[0] == largest and s[-1] == smallest:
            if s.count(largest) == 1 and s.count(smallest) == 1:
                return 3

        return 2
