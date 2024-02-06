class Solution:
    def maxProfit(self, prices) -> int:
        arr = []
        arr.append(0)
        for i in range(len(prices)-1):
            maxNum =max(prices[i+1:])
            if maxNum-prices[i] > arr[0]:
                    arr.pop(0)
                    arr.append(maxNum-prices[i])
        return arr[0]
        
    
s = Solution()
print(s.maxProfit([1,2]))