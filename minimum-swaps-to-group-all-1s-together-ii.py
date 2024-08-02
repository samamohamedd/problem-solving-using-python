class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        total_ones = nums.count(1)
        nums= nums+nums

        # Check if all 1s are already grouped
        if total_ones == nums[:total_ones].count(1):
            return 0

        left = 0
        zeros = nums[:total_ones].count(0)
        min_swaps = zeros

        for right in range(total_ones, len(nums)):
            if nums[right] == 0:
                zeros += 1
            if nums[left] == 0:
                zeros -= 1
            left += 1
            min_swaps = min(min_swaps, zeros)

        return min_swaps

