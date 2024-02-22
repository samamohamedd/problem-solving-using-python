class solution:
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
    
s = solution()
print(s.productExceptSelf([-1,1,0,-3,3]))
