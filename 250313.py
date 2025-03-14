from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def can_zero_with_k(k: int) -> bool:
            n = len(nums)
            diff = [0] * (n + 1) 
            
            for i in range(k):
                l, r, val = queries[i]
                diff[l] -= val
                diff[r + 1] += val 
            
            decrement = [0] * n
            curr_decrement = 0
            for i in range(n):
                curr_decrement += diff[i]
                decrement[i] = curr_decrement

            for i in range(n):
                if nums[i] + decrement[i] > 0:
                    return False
            return True
        
        left, right = 0, len(queries)
        answer = -1

        while left <= right:
            mid = (left + right) // 2
            if can_zero_with_k(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1 
        
        return answer
