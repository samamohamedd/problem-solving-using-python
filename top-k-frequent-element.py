class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items(): #n occurs c number of times
            freq[n].append(n) 

        result = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
    
# O(n)
s = Solution()
print(s.topKFrequent([1,1,1,2,2,3],2))