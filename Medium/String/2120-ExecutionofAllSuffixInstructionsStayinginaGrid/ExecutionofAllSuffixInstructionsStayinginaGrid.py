from typing import List

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans = []
        startY, startx = startPos
        for r in range(len(s)):
            x, y = startx, startY
            count = 0
            for c in range(r, len(s)):
                if s[c] == "R":
                    if x + 1 < n:
                        x += 1
                        count += 1
                    else:
                        break
                elif s[c] == "D":
                    if y + 1 < n:
                        y += 1
                        count += 1
                    else:
                        break
                elif s[c] == "L":
                    if x - 1 >= 0:
                        x -= 1
                        count += 1
                    else:
                        break
                elif s[c] == "U":
                    if y - 1 >= 0:
                        y -= 1
                        count += 1
                    else:
                        break
            ans.append(count)
        return ans

result = Solution()
result.executeInstructions( n = 3, startPos = [0,1], s = "RRDDLU")
