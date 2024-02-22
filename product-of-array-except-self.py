class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        multiple = 1
        answer = []
        for i in range(len(nums)):
            temp = nums
            temp.pop(i)
#            answer.append(int(np.prod(nums)))
        return answer
    
class olution:
    def productExceptSelf(self, nums):
        multiple = 1
        answer = []
        for num in nums : multiple *= num
        for num in nums:
            if num == 0 :
                nums2 = nums.copy()
                nums2.remove(num)
                mul=1
                for num in nums2 : mul *= num
                answer.append(mul)
            else:
                answer.append(int(multiple/num))
        return answer
    
s = olution()
print(s.productExceptSelf([-1,1,0,-3,3]))
