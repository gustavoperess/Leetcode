from typing import List
class Solution:
    def count_subarrays(self, arr):
        n = len(arr)
        res = [1] * n
        stack = [-1]
        #left
        for i in range(n):
            while len(stack) > 1 and arr[stack[-1]] < arr[i]:
                stack.pop()
                res[i] += i - stack[-1] - 1
                stack.append(i)
            
        # from right
        stack = [n]
        for i in range(n - 1, -1, -1):
            while len(stack) > 1 and arr[stack[-1]] < arr[i]:
                stack.pop()
                res[i] += stack[-1] - i - 1
                stack.append(i)
        return res
    
    def min_length_substring(self, s, t):
        if t == "": 
            return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT)
        res, reslen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = (r - l + 1)

                if s[l] in countT:
                    if window[s[l]] == countT[s[l]]:  
                        have -= 1
                    window[s[l]] -= 1  

                l += 1

        return s[res[0]:res[1] + 1] if reslen != float("infinity") else ""
    
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        count = 0
        for i in s:
            if i == "(":
                stack.append(i)
                count += 1
            elif i == ")" and count > 0:
                stack.append(i)
                count -= 1
            elif i != ")":
                stack.append(i)
        filtered = []
        for i in reversed(stack):
            if i == "(" and count > 0:
                count -= 1
            else:
                filtered.append(i)
            
        return "".join(filtered[::-1])
                
                
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "}" : "{","]" : "[", }
        for i in s:
            if i in closeToOpen:
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else True
        
    def maxScore(self, s: str) -> int:
        ans = 0
        count_zeros_left = 0
        count_ones_right = len([i for i in s if i == '1'])
        for i in range(len(s) - 1):
            count_zeros_left += s[i] == '0'
            count_ones_right -= s[i] == '1'
            ans = max(ans, count_ones_right + count_zeros_left)
  
        return ans
    
    def are_they_equal(self, array_a, array_b):
        if len(array_a) != len(array_b):
            return False    
        hashMapOne = {}
        hashMapTwo = {}
        for i in range(len(array_a)):
            if array_a[i] in hashMapOne:
                hashMapOne[array_a[i]] += 1
            else:
                hashMapOne[array_a[i]] = 1
            if array_b[i] in hashMapTwo:
                hashMapTwo[array_b[i]] += 1
            else:
                hashMapTwo[array_b[i]] = 1
            
            for key, value in hashMapOne.items():
                if hashMapOne[key] != hashMapTwo.get(key, 0):
                    return False
        return True

    def rotationalCipher(self, input_str, rotation_factor):
        result = ""
        for i, v in enumerate(input_str):
            if v.isalpha():
                t = ord(v.lower()) - 96
                new_t = (t + rotation_factor) % 26
                if new_t == 0:
                    new_t = 26
                new_char = chr(new_t + 96)
                if v.isupper():
                    new_char = new_char.upper()
                result += new_char
            elif v.isnumeric():
                result += str((int(v) + rotation_factor) % 10)
            else:
                result += v
        return result
    
    def isPalindrome(self, x: int) -> bool:
        reversed_num = 0
        temp = x
        
        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10
        return reversed_num == x

    def countPalindromicSubsequence(self, s: str) -> int:
        rightS = {}
        leftS = set()
        result = set()
        for i in s:
            if i in rightS:
                rightS[i] += 1
            else:
                rightS[i] = 1
        for i,m in enumerate(s):
            rightS[m] -= 1
            for c in leftS:
                if rightS[c] > 0:
                    result.add((c,m))
            leftS.add(m)

        return result
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            string1 = s[:left] + s[left+1:]
            if s[left] != s[right]:
                string1 = s[:left] + s[left+1:]
                string2 = s[:right] + s[right+1:]
                return string1==string1[::-1] or string2==string2[::-1]
            left += 1
            right -= 1
        return True
    
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_ptr = abbr_ptr = 0
        while word_ptr < len(word) and abbr_ptr < len(abbr):
            if abbr[abbr_ptr].isdigit():
                if abbr[abbr_ptr] == '0':
                    return False
                steps = 0
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    steps = steps * 10 + int(abbr[abbr_ptr]) # converting to int
                    abbr_ptr += 1
                word_ptr += steps
            else:    
                if word[word_ptr] != abbr[abbr_ptr]:
                    return False
                word_ptr += 1
                abbr_ptr += 1
        return word_ptr == len(word) and abbr_ptr == len(abbr)
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1] 
                n -= 1
            last -= 1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1

    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 1
        dec = 1
        ans = 1
        for i in range(len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
            ans = max(inc, dec)
        return ans

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i
        return [0,0]
    
    def toGoatLatin(self, sentence: str) -> str:
        ans = []
        vowels = ['a','e','i','o','u',]
        s = sentence.split(" ")
        for i in range(len(s)):
            if s[i][0].lower() in vowels:
                ans.append(s[i] + "ma" + ((i + 1) * 'a'))
            else:
                ans.append(s[i][1:] + s[i][0] + "ma" + ((i + 1) * 'a'))
            
        return " ".join(ans)
    
    def addStrings(self, num1: str, num2: str) -> str:
        def convertToInd(number):
            hashMap = { '0':0,
                        '1':1,
                        '2':2,
                        '3':3,
                        '4':4,
                        '5':5,
                        '6':6,
                        '7':7,
                        '8':8,
                        '9':9
                    }
            ans = 0
            for i in number:
                ans = ans * 10 + hashMap[i]
            return ans
        return str(convertToInd(num1) + convertToInd(num2))
    
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        prevRows = self.generate(numRows - 1)
        newRow = [1] * numRows
        
        for i in range(1, numRows- 1):
            newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]
     
        prevRows.append(newRow)
        return prevRows
    
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def isDiagonal(row, col):
            val = matrix[row][col]
            
            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != val:
                    return False
                row += 1
                col += 1
            return True
        
        for col in range(len(matrix[0])):
            if not isDiagonal(0, col):
                return False
            
        for row in range(1, len(matrix)):
            if not isDiagonal(row, 0):
                return False
        return True
    
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ans = []
        # for i in range(len(nums) - 1):
        #     if nums[i] +1 != nums[i + 1]:
        #         ans.append([nums[i] + 1, nums[i + 1] - 1])
        # ans.append([nums[-1] + 1, upper]) 
        # return ans
        for num in nums:
            if num > lower:
                ans.append([lower, num - 1])
            lower = num + 1
        if lower <= upper:
            ans.append([lower, upper])
        
        return ans
  
    def intToRoman(self, num: int) -> str:
        hashMap = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        res = []
        for key, value in hashMap.items():
            if num == 0:
                break
            count = num // key
            res.append(value * count)
            num -= count * key
        
        return "".join(res)
    
                    
    def binarySearch(self, numbers: List[int], toFind: int) -> bool: 
        l,r = 0, len(numbers) - 1
        while l <= r:
            mid = (l + r) // 2
            if numbers[mid] < toFind:
                l = mid + 1
            elif numbers[mid] > toFind:
                r = mid - 1 
            else:
                return True
        return False
        
        
        
result = Solution()


