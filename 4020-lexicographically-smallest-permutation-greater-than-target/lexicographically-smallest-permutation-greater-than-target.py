from typing import List
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1
        n = len(s)
        for i in range(n - 1,-1,-1):
            temp = count[:]
            possible = True
            for j in range(i):
                idx = ord(target[j]) - ord('a')

                if temp[idx] == 0:
                    possible = False
                    break
                temp[idx] -= 1
            if not possible:
                continue
            target_idx = ord(target[i]) - ord('a')
            for c in range(target_idx + 1, 26):
                if temp[c] > 0:
                    temp[c] -= 1
                    ans = target[:i] + chr(c + ord('a'))

                    for x in range(26):
                        ans += chr(x+ord('a')) * temp[x]
                    return ans
        return ""
        