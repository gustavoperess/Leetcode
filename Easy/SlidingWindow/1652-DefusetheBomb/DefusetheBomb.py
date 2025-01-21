
from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        l = len(code)
        ans = [0] * l
        if k == 0:
            return ans
        if k > 0:
            ans[0]=wsum=sum(code[1:k+1])
            for i in range(1, l):
                r = (i + k) % l
                wsum+=-code[i]+code[r]
                ans[i]=wsum
        else:
            ans[0]=wsum=sum(code[-1:k-1:-1])
            for i in range(1, l):
                r = (i - k) % l
                wsum+=-code[-i]+code[-r]
                ans[-i]=wsum
                print(r, code[r], wsum)
        return ans
      


result = Solution()
# result.decrypt(code = [5,7,1,4], k = 3)
result.decrypt(code = [2,4,9,3], k = -2)