from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = defaultdict(int)

        #store frequencies of numbers
        for num in nums:
            freq[num] +=1

        #converting the dict into list of key-value pairs
        freq_list = list(freq.items())

        #This lambda function extracts the second element (frequency) from each element in the list.
        #Sort the list based on the frequency (value) in descending order
        freq_list.sort(key= lambda x : x[1], reverse=True)
        print(freq_list)
        
        result = [item[0] for item in freq_list[:k]]
        return result
# O(n)
s = Solution()
print(s.topKFrequent([1,1,1,2,2,3],2))