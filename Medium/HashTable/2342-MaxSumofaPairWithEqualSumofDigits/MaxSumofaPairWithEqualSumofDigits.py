from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hashMap = {}
        for k,v in enumerate(nums):
            splited = sum([int(i) for i in str(v)])
            if splited in hashMap:
                hashMap[splited].append(v)
            else:
                hashMap[splited] = [v]
        ans = 0        
        for i in hashMap.values():
            if len(i) > 1:
                i.sort(reverse=True)
                max_pair_sum = i[0] + i[1]
                ans = max(ans, max_pair_sum)
        
        return ans if ans != 0 else -1

        


result = Solution()
(result.maximumSum(nums = [18,43,36,13,7]))
# (result.maximumSum(nums = [10,12,19,14]))