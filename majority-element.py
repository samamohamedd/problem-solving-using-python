#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
from typing import Dict
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dict :Dict[int,int] ={}
        n = len(nums)
        for i in nums:
            if i in dict.keys():
                dict[i] = dict[i] +1
            else: dict[i] = 1
            if dict[i] > n/2 :
                return i    
            
        return i    