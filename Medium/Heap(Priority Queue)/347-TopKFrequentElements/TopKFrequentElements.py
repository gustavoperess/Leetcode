from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for n in nums:
            if n in hashMap:
                hashMap[n] += 1
            else:
                hashMap[n] = 1
        
        s = [ (-v, i) for i, v in hashMap.items()]
        heapq.heapify(s)
        ans = []
        while k > 0:
            i, v = heapq.heappop(s)
            ans.append(v)
            k -= 1
        
        return ans

    def findKthLargest(self, nums: List[int], k: int) -> int:
        s = [-i for i in nums]
        heapq.heapify(s)
        ans = 0
        while k > 0:
            q = heapq.heappop(s)
            ans = -q
            k -= 1
        
        return ans
    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashMap = {}
        for w in words:
            if w in hashMap:
                hashMap[w] += 1
            else:
                hashMap[w] = 1
        s = [ ((-v,i))  for i, v in hashMap.items()]
        heapq.heapify(s)
        ans = []
        while k > 0:     
            i,v = heapq.heappop(s)
            ans.append(v)
            k -= 1
        return ans

    def mostFrequentEven(self, nums: List[int]) -> int:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                if nums[i] in hashMap:
                    hashMap[nums[i]] += 1
                else:
                    hashMap[nums[i]] = 1
        

        if len(hashMap) == 0:
            return -1
        
        return sorted(hashMap.items(), key=lambda x:(x[1], -x[0]) , reverse=True)[0][0]
        
        

    
    
result = Solution()
#result.topKFrequent( nums = [1,1,1,2,2,3], k = 2)
# result.findKthLargest(nums = [3,2,1,5,6,4], k = 2)
#result.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2)
result.mostFrequentEven(nums = [0,1,2,2,4,4,1])
#result.topKFrequent( words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4)