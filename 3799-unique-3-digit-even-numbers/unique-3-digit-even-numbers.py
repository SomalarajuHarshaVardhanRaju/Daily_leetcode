from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = [0] * 10

        # Count available copies of each digit
        for d in digits:
            count[d] += 1

        ans = 0

        for num in range(100, 1000, 2):
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            # Check whether we have enough copies
            if a == b == c:
                if count[a] >= 3:
                    ans += 1

            elif a == b:
                if count[a] >= 2 and count[c] >= 1:
                    ans += 1

            elif a == c:
                if count[a] >= 2 and count[b] >= 1:
                    ans += 1

            elif b == c:
                if count[b] >= 2 and count[a] >= 1:
                    ans += 1

            else:
                if count[a] >= 1 and count[b] >= 1 and count[c] >= 1:
                    ans += 1

        return ans