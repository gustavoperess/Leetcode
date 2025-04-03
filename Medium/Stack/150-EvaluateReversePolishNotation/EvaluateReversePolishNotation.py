
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif i == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            elif i == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            elif i == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            else:
                stack.append(int(i))                
        
        return stack[0]
    
   

        
result = Solution()
result.evalRPN(tokens = ["2","1","+","3","*"])
result.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])