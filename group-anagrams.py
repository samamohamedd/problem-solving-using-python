from collections import Counter


class Solution:
    def groupAnagrams(self, strs):
        finalList = []
        if len(strs) <= 1: return [strs]
        finalList.append([strs[0]])
        for i in range(1,len(strs)): 
            for innerlist in finalList:
                if Counter(strs[i]) == Counter(innerlist[0]):
                    innerlist.append(strs[i])
                    break    
            else:
                finalList.append([strs[i]])
        return finalList
            
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))