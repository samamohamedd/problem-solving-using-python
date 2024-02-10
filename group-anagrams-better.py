class Solution:
    def groupAnagrams(self, strs):
        answer = {} #mapping charcount to list of anagrams

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1

            answer[tuple(count)].append(word)

        return answer.values()