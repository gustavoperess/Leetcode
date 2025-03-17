from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
            hashMap = {}
            l = 0
            result = [0] * (len(nums) - k + 1)
            for i in range(len(nums)):
                if nums[i] in hashMap:
                    hashMap[nums[i]] += 1
                else:
                    hashMap[nums[i]] = 1

                
                while sum(hashMap.values()) == k:
                    ans = 0
                    sortedArr = sorted(hashMap.items(), key=lambda x:(x[1], x[0]), reverse=True)[:x]
                    for t in sortedArr:
                        ans += t[0] * t[1]
                    result[l] = ans
                    hashMap[nums[l]] -= 1
                    if hashMap[nums[l]] == 0:
                        del hashMap[nums[l]]
                    l += 1
            
            return result



result = Solution()
# result.maximumLengthSubstring(s = "bcbbbcba")
# result.divideArray(nums = [3,2,3,2,2,2])
