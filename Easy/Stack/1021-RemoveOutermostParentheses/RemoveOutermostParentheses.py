



class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        popen = 0
        stack = []
        for x in s:
            if x == ")":
                print(popen,x)
                popen -= 1
            if popen > 0:
                stack.append(x)
            if x == "(":
                print(popen,x)
                popen += 1




result = Solution()
result.removeOuterParentheses(s = "(()())(())")