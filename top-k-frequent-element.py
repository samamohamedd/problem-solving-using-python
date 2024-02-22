from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        answer = defaultdict(int)
        for n in nums:
            if n in answer:
                answer[n] += 1
            else:
                answer[n] = 1
        answerlist = sorted(answer.values(), reverse=True)
        if len(answerlist)==0:
            return answerlist
        listt = []
        for i in answerlist:
            answer.get
        answerlist = answerlist[:k]

        return answerlist
    
s = Solution()
print(s.topKFrequent([1,1,1,2,2,3],2))