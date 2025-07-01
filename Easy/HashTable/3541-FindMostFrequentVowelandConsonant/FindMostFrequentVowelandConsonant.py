from typing import List
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = {'a','e','i','o','u'}
        vow = [0] * 26
        const = [0] * 26
        for i in s:
            idx = ord(i) - ord('a')
            if i in vowel:
                vow[idx] += 1
            else:
                const[idx] += 1
        return max(vow) + max(const)

    def longestSubsequence(self, s: str, words: List[str]) -> int:
        s_freq = {}
        for char in s:
            if char in s_freq:
                s_freq[char] += 1
            else:
                s_freq[char] = 1
                
        for word in words:
            word_freq = {}
            for char in word:
                if char in word_freq:
                    word_freq[char] += 1
                else:
                    word_freq[char] = 1
            
            can_form =True
            for c in word_freq:
               # print(c, s_freq, word_freq[char], s_freq[char], word)
                if c not in s_freq or word_freq[char] > s_freq[char]:
                    can_form = False
                    break
            
            if can_form:
                print(word)
        
            
result = Solution()
#result.maxFreqSum( s = "successes")
result.longestSubsequence(s = "abcde",words = ["a", "bb", "acd", "ace", "ba"])
#result.maxFreqSum( s = "aeiaeia")