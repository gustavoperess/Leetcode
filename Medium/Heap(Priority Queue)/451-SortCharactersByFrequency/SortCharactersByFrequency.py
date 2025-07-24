import heapq
from typing import List
class Solution:
    def frequencySort(self, s: str) -> str:
        hashMap = {}
        for i in s:
            hashMap[i] = 1 + hashMap.get(i, 0)
            
        pq = [(-freq, char) for char, freq in hashMap.items()]
        heapq.heapify(pq)

        ans = ""
        while pq:
            x = heapq.heappop(pq)
            t = (x[0] * -1) * x[1]
            ans += t
        return ans
    
    def minSetSize(self, arr: List[int]) -> int:
        hashMap = {}
        h = len(arr) // 2
        for i in range(len(arr)):
            if arr[i] in hashMap:
                hashMap[arr[i]] += 1
            else:
                hashMap[arr[i]] = 1
        minSizer = float("inf")
        for k,v in hashMap.items():
            if h - v in hashMap.values():
                for key, value in hashMap.items():
                    if h-v == value:
                        minSizer = min(minSizer, len([k, key]))
        
        if minSizer == "inf":
            return 1
        return minSizer

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            last = ans[-1][1]
            if intervals[i][0] <= last:        
                ans[-1][-1] = max(last, intervals[i][-1])
            else:
                ans.append(intervals[i])
        
        return ans
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s = 0
        for i in range(len(intervals)):
            if intervals[i][0] < newInterval[0]:
                s = i + 1
        intervals.insert(s, newInterval)
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            last = ans[-1][1]
            if intervals[i][0] <= last:
                ans[-1][-1] = max(last, intervals[i][-1])
            else:
                ans.append(intervals[i])

        return ans
    
    def stringMatching(self, words: List[str]) -> List[str]:
        s = " ".join(words)
        result = []
        for w in words:
            ct = s.count(w)
            if ct >= 2:
                result.append(w)
        return result


result = Solution()
result.stringMatching(words = ["mass","as","hero","superhero"])

        