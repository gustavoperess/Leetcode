

class Solution:
    def isValid(self, s: str) -> bool:
        stack   = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:             
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        print(stack)
        return True if not stack else False
        



result = Solution()
#result.isValid(s = "((()))[]{}")
result.isValid(s="[")