from typing import Dict
def solution(theList: list[int]) -> str:
   counts:Dict[int,int] ={}
   for element in theList:
      if element in counts:
         return str(element)
      counts[element]=1
   return "undefined"      

print(solution([5,2,1,5,4]))
