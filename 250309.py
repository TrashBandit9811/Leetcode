from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        count = 0
        valid = 0 
        
        for i in range(k - 1):
            if colors[i] != colors[i + 1]:
                valid += 1
        
        if valid == k - 1:
            count += 1

        for i in range(1, n):
            if colors[i - 1] != colors[(i - 1 + 1) % n]:  
                valid -= 1
            
            if colors[(i + k - 2) % n] != colors[(i + k - 1) % n]:  
                valid += 1
            
            if valid == k - 1:
                count += 1
        
        return count
