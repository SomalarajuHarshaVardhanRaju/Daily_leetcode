class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Check if palindrome is possible
        odd = 0
        middle = ''

        for i in range(26):
            if freq[i] % 2:
                odd += 1
                middle = chr(i + ord('a'))

        if odd > 1:
            return ""

        # Count for the left half
        half = [x // 2 for x in freq]
        m = n // 2

        # ------------------------------------------------
        # Build palindrome from a left half
        # ------------------------------------------------
        def build(left):
            if n % 2 == 0:
                return left + left[::-1]
            else:
                return left + middle + left[::-1]

        # ------------------------------------------------
        # Try to construct the lexicographically smallest
        # palindrome greater than target.
        # ------------------------------------------------

        # We first try to make the left half equal to target's
        # first half.
        cnt = half[:]
        prefix = []

        for i in range(m):
            x = ord(target[i]) - ord('a')

            if cnt[x] == 0:
                break

            cnt[x] -= 1
            prefix.append(target[i])

        # ------------------------------------------------
        # Important:
        # If we can construct the complete target prefix,
        # check whether changing the middle can make it larger.
        # ------------------------------------------------
        if len(prefix) == m:

            # Odd length:
            # same left half, but a larger middle character
            # makes the palindrome larger.
            if n % 2 == 1:
                target_middle = target[m]

                if middle > target_middle:
                    return build(''.join(prefix))

            # If the target itself is not a palindrome,
            # compare the palindrome having the same left half.
            candidate = build(''.join(prefix))

            if candidate > target:
                return candidate

        # ------------------------------------------------
        # Now change the left half.
        #
        # We start from the RIGHT because we want the smallest
        # possible string greater than target.
        # ------------------------------------------------
        for pos in range(m - 1, -1, -1):

            cnt = half[:]

            # Match target's prefix before pos
            possible = True

            for j in range(pos):
                x = ord(target[j]) - ord('a')

                if cnt[x] == 0:
                    possible = False
                    break

                cnt[x] -= 1

            if not possible:
                continue

            current = ord(target[pos]) - ord('a')

            # Pick the smallest character > target[pos]
            for x in range(current + 1, 26):

                if cnt[x] == 0:
                    continue

                cnt[x] -= 1

                left = target[:pos] + chr(x + ord('a'))

                # Fill remaining characters in sorted order
                for c in range(26):
                    left += chr(c + ord('a')) * cnt[c]

                result = build(left)

                if result > target:
                    return result

                cnt[x] += 1

        return ""