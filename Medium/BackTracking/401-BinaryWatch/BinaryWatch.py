from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        LED_NUM = 10
        HOUR_LED_NUM = 4
        result = []
        def dfs(num: int, pos: int, hour: int, minute: int):
            if hour > 11 or minute > 59:
                return
            
            if num == 0:
                result.append("{:d}:{:02d}".format(hour, minute))
                return
            
            for i in range(pos, LED_NUM):
                if i < HOUR_LED_NUM:
                    dfs(num - 1, i + 1, hour + 2**i, minute)
                else:
                    dfs(num - 1, i + 1, hour, minute + 2**(i - HOUR_LED_NUM))
            
   
            
        dfs(turnedOn,0,0,0)
                 
                                
        

        
result = Solution()
result.readBinaryWatch(turnedOn=2)


