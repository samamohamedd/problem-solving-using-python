import math
from typing import Dict
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        x = math.floor(len(nums)/3)
        dict:Dict[int,float] = {}
        thelist= []
        for number in nums:
            if number in dict.keys():
                dict[number] = dict[number] +1
            else: dict[number] = 1
            if dict[number] > x :
                if number not in thelist : thelist.append(number)

        return thelist
