class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for n in range(len(nums)-1):
            if nums[n]==nums[n+1]:
                nums[n]=nums[n]*2
                nums[n+1]=0
                n=n+1

        non_zero_index=0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1
        return nums

solution = Solution()
nums = [1, 2, 2, 1, 1, 0]
print(solution.applyOperations(nums))