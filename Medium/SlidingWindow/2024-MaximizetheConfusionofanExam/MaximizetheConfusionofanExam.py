class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutive(char):
            l, max_count, count = 0, 0, 0
            for r in range(len(answerKey)):
                if answerKey[r] != char:
                    count += 1
                while count > k:
                    if answerKey[l] != char:
                        count -= 1
                    l += 1
                max_count = max(max_count, r - l + 1)
            return max_count
        
        return max(maxConsecutive("T"), maxConsecutive("F"))
    
    

result = Solution()
result.maxConsecutiveAnswers(answerKey = "TTFTTTTTFT", k = 1)