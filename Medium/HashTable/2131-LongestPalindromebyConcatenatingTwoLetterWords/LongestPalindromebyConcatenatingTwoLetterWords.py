from collections import defaultdict
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        m = defaultdict(int)
        unpaired = ans = 0
        for w in words:
            if w[0] == w[1]:
                if m[w] > 0:
                    unpaired -= 1
                    m[w] -= 1
                    ans += 4
                else:
                    m[w] += 1
                    unpaired += 1
            else:
                if m[w[::-1]] > 0:
                    ans += 4
                    m[w[::-1]] -= 1
                else:
                    m[w] += 1
        if unpaired > 0:
            ans += 2
        return ans
                
       


result = Solution()
#result.longestPalindrome(words = ["ab","ty","yt","lc","cl","ab"])
result.longestPalindrome(words = ["cc","ll","xx"])
#result.longestPalindrome(words = ["lc","cl","gg"])