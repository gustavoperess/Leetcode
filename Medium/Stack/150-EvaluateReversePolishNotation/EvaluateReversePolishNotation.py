
from typing import List
import math

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
            

    def calculate(self, s: str) -> int:
        numbers  = []
        for i in s:
            if i != " ":
                numbers.append(f"{i}")
        stack = []
        i = 0
        while i < len(numbers):
            if numbers[i] == "+":
                a = stack.pop()
                b = int(numbers[i + 1])
                stack.append(a + b)
                i += 1
            elif numbers[i] == "-":
                a = stack.pop()
                b = int(numbers[i + 1])
                stack.append(b - a)
                i += 1
            else:
                stack.append(int(numbers[i]))
            i += 1
        
        print(stack)
        
result = Solution()
#result.evalRPN(tokens = ["2","1","+","3","*"])
#result.calculate( s = "(1+(4+5+2)-3)+(6+8)")
#result.calculate( s = "4+5+2")
result.calculate(s = "1+4+5+2-3+6+8")
#result.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])