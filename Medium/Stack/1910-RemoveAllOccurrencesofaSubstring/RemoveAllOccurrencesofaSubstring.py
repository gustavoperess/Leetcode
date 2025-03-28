




class Solution:
    def removeOccurrencesOne(self, s: str, part: str) -> str:
        while part in s:
            print(s)
            s = s.replace(part, "", 1)  
        return s
    
    def removeOccurrences(self, s: str, part: str) -> str:
        result_stack = []
        target_end_char = part[-1]
        x = len(part)
        for current_char in s:
            result_stack.append(current_char)
            if current_char == target_end_char and len(result_stack) >= x:
                if "".join(result_stack[-x:]) == part:
                    del result_stack[-x:]
        
        return "".join(result_stack)
        
        
result = Solution()
result.removeOccurrences(s = "daabcbaabcbc", part = "abc")
#result.removeOccurrences( s = "axxxxyyyyb", part = "xy")