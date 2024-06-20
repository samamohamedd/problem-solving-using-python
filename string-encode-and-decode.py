class Solution:

    def encode(self, strs: list[str]) -> str:
        if len(strs)==0 : return ""
        
        str = strs[0]
        for x in range(1, len(strs)):
            str += f" {strs[x]}"
        return str

    def decode(self, s: str) -> list[str]:
        #if self.encode()
        if s is None : return []
        if s == '': return [""]
        strlist = list(s)
        words =[strlist[0]] 
        for x in range (1, len(strlist)):
            #if letter == strlist[0]: continue

            if strlist[x] == " ":
                words.append("")
            else: words[-1] +=  strlist[x]
        return words
    
s = Solution()

print(s.encode(["#","##"]))
print(s.decode("# ##"))