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
    def countLargestGroup(self, n: int) -> int:
        def count_i(x):
            t = 0
            while x > 0:
                t += x % 10
                x //= 10
            return t
        hashMap = {}
        for i in range(1, n + 1):
            s = count_i(i)
            if s in hashMap:
                hashMap[s] += 1
            else:
                hashMap[s] = 1
                
        m = max(hashMap.values())
        count = 0
        
        for i in hashMap.values():
            if i == m:
                count += 1
        
        return count
    
    
    def loteteryProblem(self, entries) -> int:
        # organizing a lottery for 1589 people 
        # win if they do not share their birthday
        # enter their lottery using their birthday and the ticket number
        # wins if the birthday is not shared 
        # if multiple people do share the same birthday date, prize is divided. 
        # if no one has a unique birthday, no one wins. 
        hashMap = {}
        for birthday, ticketNumber in entries:
            k = int("".join(birthday.split("/")))
            hashMap[k].append(ticketNumber)

        winners = {}
        for birthday, tickets in hashMap.items():
            if len(tickets) == 1:
                winners[tickets[0]] = "Full Prize"
            else:
                for t in tickets:
                    winners[t] = f"Shared Prize among {len(tickets)} people"
        return winners if winners else "No winners"


result = Solution()
# result.findSubstring(s = "foobarfoobar", words = ["foo","bar"])
result.findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","good"])
result.countLargestGroup(n = 14)
#result.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"])
#result.findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"])
    