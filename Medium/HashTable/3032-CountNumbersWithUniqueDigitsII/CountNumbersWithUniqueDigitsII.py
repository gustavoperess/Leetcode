class Solution:
    def numberCount(self, a: int, b: int) -> int:
        ans = 0
        for i in range(a, b + 1):
            k = str(i)
            x = set(k)
            if len(x) == len(k):
                ans += 1
        return ans

    def calculateTime(self, keyboard: str, word: str) -> int:
        hashMap = {}
        for key, value in enumerate(keyboard):
            hashMap[value] = key
        ans = 0
        totalTime = 0
        for w in word:
            j = hashMap[w]
            ans += (abs(j - totalTime))
            totalTime = j
        return ans

result = Solution()
result.calculateTime(keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode")