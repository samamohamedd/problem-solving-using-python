class Solution:
    def twoSum(self, nums, target: int) :
        for i in range(len(nums)):
            for j in range(i+1,len(nums)-1):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [0,0]
    
s = Solution()
print(s.twoSum([2,5,5,11],10))