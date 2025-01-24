from typing import List
import math

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # t = len("".join(words))
        # print(math.ceil(t / maxWidth), t)
        # print(35 / 3)
        # print(len("Whatmustbe") - 16)
        # print(len("acknowledgment") - 16)
        # print(len("shallbe") - 16)
        print((15 * 70))
        pass
    
    


result = Solution()
result.fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16)
# result.fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16)

# result.fullJustify(words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20)