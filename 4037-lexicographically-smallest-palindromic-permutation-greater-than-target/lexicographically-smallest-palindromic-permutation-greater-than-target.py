class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        odd = 0
        middle = ''

        for i in range(26):
            if freq[i] % 2:
                odd += 1
                middle = chr(i + ord('a'))

        if odd > 1:
            return ""

        half = [x // 2 for x in freq]
        m = n // 2

        def build(left):
            if n % 2 == 0:
                return left + left[::-1]
            else:
                return left + middle + left[::-1]

        cnt = half[:]
        prefix = []

        for i in range(m):
            x = ord(target[i]) - ord('a')

            if cnt[x] == 0:
                break

            cnt[x] -= 1
            prefix.append(target[i])

        if len(prefix) == m:

            if n % 2 == 1:
                target_middle = target[m]

                if middle > target_middle:
                    return build(''.join(prefix))

            candidate = build(''.join(prefix))

            if candidate > target:
                return candidate
    
        for pos in range(m - 1, -1, -1):

            cnt = half[:]

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

            for x in range(current + 1, 26):

                if cnt[x] == 0:
                    continue

                cnt[x] -= 1

                left = target[:pos] + chr(x + ord('a'))

                for c in range(26):
                    left += chr(c + ord('a')) * cnt[c]

                result = build(left)

                if result > target:
                    return result

                cnt[x] += 1

        return ""