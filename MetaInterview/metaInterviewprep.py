from collections import Counter


def rotationalCipher(input_str, rotation_factor):
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


rotationalCipher("Zebra-493?", 3)
rotationalCipher("abcdefghijklmNOPQRSTUVWXYZ0123456789", 39)


def are_they_equal(array_a, array_b):
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

are_they_equal(array_a = [1, 2, 3, 1], array_b = [1, 4, 3, 2])


def count_subarrays(arr):
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
    



count_subarrays(arr = [3, 5, 4, 3, 2, 1, 7])

def min_length_substring(s, t):
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

    



t = min_length_substring(s = "adobecodebanc", t="abc")
# t = min_length_substring(s = "ab", t="a")
