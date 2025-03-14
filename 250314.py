from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        left, right = 1, max(candies)
        best = 0

        while left <= right:
            mid = (left + right) // 2
            total_children = sum(c // mid for c in candies)

            if total_children >= k:
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return best
