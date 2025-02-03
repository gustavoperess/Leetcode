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
        print(rightS)
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
          
        
result = Solution()
result.validWordAbbreviation(word = "internationalization", abbr = "i12iz4n")