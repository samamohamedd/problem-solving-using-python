class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n= len(nums)
        for i in range(0,n):
            if i in nums: continue
            return i
        return n