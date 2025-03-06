from collections import Counter
from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        flat_grid = [num for row in grid for num in row]
        counts = Counter(flat_grid)
        duplicate = next(num for num, freq in counts.items() if freq == 2)
        top = len(flat_grid) * len(flat_grid) + 1
        missing = (set(range(1,top)) - set(flat_grid)).pop()
        results=[duplicate, missing]
        return results
