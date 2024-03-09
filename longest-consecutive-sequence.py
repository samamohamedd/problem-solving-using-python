class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums) #cause it has O(1) member checking time
        longest_seq = 0
        current_num = 0
        current_seq = 0
        
        for num in nums_set:
            if num-1 not in nums_set:
                current_num = num 
                current_seq = 1

            while current_num+1 in nums_set:
                current_num += 1
                current_seq += 1
            longest_seq = max(longest_seq, current_seq)

        return longest_seq

s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))