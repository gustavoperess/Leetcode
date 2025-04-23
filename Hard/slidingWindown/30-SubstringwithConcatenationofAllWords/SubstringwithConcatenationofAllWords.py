from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []

        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words
        word_count = Counter(words)
        result = []

        for i in range(word_len):  
            left = i
            right = i
            curr_count = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    curr_count[word] += 1

                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        left += word_len

                    if right - left == total_len:
                        result.append(left)
                else:
                    curr_count.clear()
                    left = right

        return result
                
            
            
        
    


result = Solution()
# result.findSubstring(s = "foobarfoobar", words = ["foo","bar"])
result.findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","good"])
#result.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"])
#result.findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"])
    