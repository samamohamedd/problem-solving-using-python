class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        l = list(s)
        for ch in t:
            if ch in l:
                l.remove(ch)
        if len(l)==0 : return True
        return False
s = Solution()
print(s.isAnagram("anagram", "naragam"))