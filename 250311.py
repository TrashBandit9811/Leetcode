from collections import Counter

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = Counter()
        left = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while all(count[ch] > 0 for ch in "abc"):
                result += len(s) - right
                count[s[left]] -= 1
                left += 1 

        return result
