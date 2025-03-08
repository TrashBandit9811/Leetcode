class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operations = float('inf')

        for i in range(len(blocks) - k + 1):
            window = blocks[i:i + k]
            operations = window.count('W')
            min_operations = min(min_operations, operations)
        
        return min_operations
