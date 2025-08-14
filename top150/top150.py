from typing import List
import collections
import math
import heapq

class Soluiton:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        s = sorted(nums1[:m] + nums2[:n])
        for i,v in enumerate(s):
            nums1[i] = v
            
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        p1, p2 = 0, 1
        while p2 < len(prices):
            if prices[p2] > prices[p1]:
                ans = max(ans, prices[p2] - p1)
            else:
                p1 = p2
            p2 += 1
  
    def binarySearch(self, nums: List[int], n: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            midpoint = (l + r) // 2
            if nums[midpoint] == n:
                return True
            if nums[midpoint] < n:
                l = midpoint + 1
            elif nums[midpoint] > n:
                r = midpoint - 1
        return False
  
                  
    def reverseWords(self, s: str) -> str:
        x = s.split(" ")
        ans = []
        for i in x[::-1]:
            if i != "":
                ans.append(i)
        return " ".join(ans)
    
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        idx, d = 0, 0
        rows = [[] for _ in range(numRows)]
        
        for char in s:
            rows[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = - 1
            idx += d
        ans = ""
        for i in rows:
            ans += "".join(i)

        return ans
    
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        ans = float("inf")
        for r in range(len(nums)):
            right += nums[r]
            while right >= target:
                ans = min(ans, (r - left) + 1)
                right -= nums[left]
                left += 1
     
        return 0 if ans == float("inf") else ans
    
            
   
    
    def allPermutations(self, s: List[str]) -> List[str]:
        ans = [] 
        subsets = []
        def dfs():
            if len(subsets) == len(s):
                cp = "".join(subsets)
                ans.append(cp)
                return
        
            for x in s:
                if x not in subsets:
                    subsets.append(x)
                    dfs()
                    subsets.pop()
            
        dfs()
    
    def linearSearchWithRecursion(self, nums: List[str], n: int, i: int) -> bool:
        if i > len(nums) - 1:
            return False
        elif nums[i] == n:
            return True
        else:
            return self.linearSearchWithRecursion(nums, n, i + 1)
    
    def insertionSortWithRecursion(self, nums: List[str], i: int,) -> List[str]:
        if i >= len(nums):
            return nums
        min_index = i + nums[i:].index(min(nums[i:]))
        nums[i], nums[min_index] = nums[min_index], nums[i]
        return self.insertionSortWithRecursion(nums , i + 1)
    
    def kthSmallestAlgorithm(self, nums: List[str], kth: int) -> int:
        self.insertionSort(nums)
        return nums[kth]
        

    def insertionSort(self, nums: List[str]) -> None:
        for i in range(1, len(nums)):
            j = i - 1
            temp = nums[i]
            
            while j >= 0 and nums[j] > temp:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = temp    
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        y = len(stones)
        for i in range(len(stones)):
            while y >= 2:
                stones.sort()
                smash = stones[-1] - stones[-2]
                stones.pop()
                stones.pop()
                stones.append(smash)
                
                y -= 1
        print(stones)
        return stones[0]
    
    
    def binarySearch(self, nums: List[int], n:int) -> int:
        nums.sort() # in case numbers are not sorted.
        l, r, = 0, len(nums) -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == n:
                return (len(nums) - mid) - 1
            if nums[mid] < n:
                l = mid + 1
            elif nums[mid] > n:
                r = mid - 1
        return 0
    
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
        
    
    
    def quickSort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self.quickSort(array, low, pi - 1)
            self.quickSort(array, pi+ 1,  high)
    
    
    def mergeS(self, arr, left, mid, right):
        arrLeft = [0] * (mid - left + 1)
        arrRight = [0] * (right - mid)
        for i in range(len(arrLeft)):
            arrLeft[i] = arr[left + i]
        
        for i in range(len(arrRight)):
            arrRight[i] = arr[mid + 1 + i]
        
        l,r,k = 0,0,left
        while l < len(arrLeft) and r < len(arrRight):
            if arrLeft[l] <= arrRight[r]:
                arr[k] = arrLeft[l]
                l += 1
            else:
                arr[k] = arrRight[r]
                r += 1
            k += 1
                
        while l < len(arrLeft):
            arr[k] = arrLeft[l]
            l += 1
            k += 1
        while r < len(arrRight):
            arr[k] = arrRight[r]
            r += 1
            k += 1
    
    
    def mergeSort(self, arr, left , right):
        if left < right:
            mid = (left + right) // 2
        
            self.mergeSort(arr, left, mid)
            self.mergeSort(arr, mid + 1, right)
            self.mergeS(arr, left, mid, right)
            
    
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        map = collections.Counter(letters)
        ans = 0
        def dfs(i, map, currScore):
            nonlocal ans
            ans = max(ans, currScore)
            if i == len(words):
                return
            for w in range(i, len(words)):
                tmpCounter = map.copy()
                word = words[w]
                isValid = True
                count = 0
                for ch in word:
                    if ch in tmpCounter and tmpCounter[ch] > 0:
                        tmpCounter[ch] -= 1
                        count += score[ord(ch) - ord("a")]
                    else:
                        isValid = False
                        break
               
                if isValid:
                    print(count)
                    dfs(i + 1, tmpCounter, count + currScore )           


        dfs(0, map, 0)
        return ans
    
            
result = Soluiton()




def mistery(n):
    s = [0] * (n + 1)
    s[1] = 0
    for i in range(2, n + 1):
        s[i] = 1

    for p in range(2, math.isqrt(n) + 1):
        if s[p] == 1:
            for f in range(p, (n//p) + 1):
                s[f * p] = 0

    for i in range(2, n + 1):
        if s[i] == 1:
            pass
   
mistery(100)


# s = list, p = frist loop, n = number of items

def sieve_recursive(s, p, n):
    if p > math.isqrt(n):
        return

    if s[p] == 1:
        mark_multiples(s, p, p, n)

    sieve_recursive(s, p + 1, n)

def mark_multiples(s, p, f, n):
    if f > n // p:
        return

    s[f * p] = 0
    mark_multiples(s, p, f + 1, n)


def mistery_recursive(n):
    s = [0] * (n + 1)
    for i in range(2, n + 1):
        s[i] = 1
    
    sieve_recursive(s, 2, n)
    # for i,v in enumerate(s):
    #     if v == 1:
    #         print(i)
   
mistery_recursive(8)



# will always have an asnwer?
# will the array 
# if the remaining is in the hashmap, i return the has
def twoSum(nums: List[int], target: int) -> List[int]:
    if len(nums) < 2:
        return [-1,-1]
    # for i in range(len(nums)):
    #     for y in range(i + 1, len(nums)):
    #         if nums[i] + nums[y] == target:
    #             return [i, y]
    # return [-1, -1]
    hashMap = {}
    for i in range(len(nums)):
        remaining = target - nums[i]
        if remaining in hashMap:
            return [hashMap[remaining], i]
        hashMap[nums[i]] = i
    return [-1, -1]

t = twoSum(nums = [11,8,7,10], target = 9)
#t = twoSum(nums = [3,2,4], target = 6)

def maxFreq(s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    hashMap = {}    
    for i in range(len(s) - minSize  + 1):
        substring = (s[i: i + minSize])
        if len(set(substring)) <= maxLetters:
            if substring in hashMap:
                hashMap[substring] += 1
            else:
                hashMap[substring] = 1
    return max(hashMap.values()) if hashMap else 0



maxFreq(s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4)
maxFreq(s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3)


def topKFrequent(nums: List[int], k: int) -> List[int]:
    hashMap = {}
    freq = [[] for i in range(len(nums) + 1)]
    for n in nums:
        if n in hashMap:
            hashMap[n] += 1
        else:
            hashMap[n] = 1
    
    for key,value in hashMap.items():
        freq[value].append(key)
        
    result = []
    for i in range(len(freq) - 1, 0 , -1):
        for x in freq[i]:
            result.append(x)
            if len(result) == k:
                return result
        
        
    
#topKFrequent( nums = [3,1,1,1,2,2], k = 2)
topKFrequent( nums = [-1,-1], k = 1)
#topKFrequent( nums = [1], k = 1)


def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals:
       return 0
    result = []
    intervals.sort(key=lambda x:x[0])
    heapq.heappush(result, intervals[0][1])
    for i in range(1, len(intervals)):
        if  result[0] <= intervals[i][0]:
            # print(result)
            heapq.heappop(result)
            
        heapq.heappush(result, intervals[i][1])
            
    


#minMeetingRooms(intervals = [[0,30],[5,10],[15,20]])
t = minMeetingRooms(intervals = [[1,10],[2,7],[3,19],[8,12],[10,20],[11,30]])



def mergeIntervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    
    intervals.sort(key=lambda x:x[0])
    ans = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= ans[-1][1]:
            ans[-1] = [min(ans[-1][0], intervals[i][0]), max(ans[-1][1], intervals[i][1])]
        else:
            ans.append(intervals[i])
    return ans


mergeIntervals(intervals = [[1,3],[2,6],[8,10],[15,18]])
mergeIntervals(intervals = [[1,4],[4,5]])



def twoSumTws(nums: List[int], target: int) -> List[int]:
        hashMap =  {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            print(remainder)
            if remainder in hashMap:
                print(hashMap[remainder], hashMap, i)
                # return [hashMap[remainder], i]
            hashMap[nums[i]] = i



# twoSumTws(nums = [2,7,11,15], target = 9)



def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    ans = []
    i, j = 0, 0 
    
    while i < len(firstList) and j < len(secondList):
        
        
        
        if firstList[i][1] < secondList[i][1]:
            print(firstList[i][1] , secondList[j][1])
            i += 1
        else:
            j += 1



# intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]])



def quickSort(a, low, high):
    if low < high:
        pi = partition(a, low, high)
        quickSort(a, low, pi - 1)
        quickSort(a, pi + 1, high)

def partition(a, low, high):
    pivot = a[high]
    print(a[low:high])
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            swap(a, i, j)
    swap(a, i + 1, high)        
    return i + 1


def swap(a, i, j):
    a[i],a[j] = a[j], a[i]
    
A = [10,5,8,3,6]
t = quickSort(A, 0, len(A) - 1)
print(A)