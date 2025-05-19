
from typing import List

class Solution:
    def largestTimeFromDigitsOne(self, arr: List[int]) -> str:
        path = []
        used = [False] * len(arr)
        res = []
        def dfs():
            if len(path) == len(arr):
                res.append("".join(path.copy()))
                return
            
            for i in range(len(arr)):
                if used[i]:
                    continue
                if len(path) == 1 and int(f"{path[-1]}{arr[i]}") > 23:
                    continue
                if len(path) == 3 and int(f"{path[-1]}{arr[i]}") > 59:
                    continue 
                         
                used[i] = True
                path.append(str(arr[i]))
                dfs()
                path.pop()
                used[i] = False

            
        dfs()
        m = max(res)
        if len(m) == 4:
            one = "".join(m[0:2])
            two = "".join(m[2:4])
            return f"{one}:{two}"
        return ""
    
    
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        path = []
        used = [False] * len(arr)
        max_time = [-1]
        def dfs():
            if len(path) == len(arr):
                hour = path[0] * 10 + path[1]
                minute = path[2] * 10 + path[3]  
                if hour < 24 and minute < 60:
                    total_minutes = hour * 60 + minute
                    max_time[0] = max(max_time[0], total_minutes)
                return
            
            for i in range(len(arr)):
                if not used[i]:
                    used[i] = True
                    path.append(arr[i])
                    dfs()
                    path.pop()
                    used[i] = False

            
        dfs()
        if max_time[0] == -1:
            return ""
        return f"{max_time[0] // 60:02}:{max_time[0] % 60:02}"


result = Solution()
result.largestTimeFromDigits(arr = [1,2,3,4])
#result.largestTimeFromDigits(arr = [0,0,0,0])
#result.largestTimeFromDigits(arr = [5,5,5,5])