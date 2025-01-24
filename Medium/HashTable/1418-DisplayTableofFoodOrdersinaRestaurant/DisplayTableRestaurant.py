from typing import List

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        hashMap = {}
        meal = set()
        for i in orders:
            meal.add(i[-1])
            if i[1] in hashMap:
                hashMap[i[1]].append(i[-1])
            else:
                hashMap[i[1]] = [i[-1]]
        so = sorted(meal)
        so.insert(0, "Table")
        newHashMap = {}   
        for k, v in hashMap.items():
            for y in range(len(v)):
                if v[y] in so:
                    if k not in newHashMap: 
                        newHashMap[k] = [0] * len(so)  
                    idx = so.index(v[y])  
                    newHashMap[k][0] = str(k) 
                    newHashMap[k][idx] += 1 
        for key in newHashMap:
            newHashMap[key] = [str(x) for x in newHashMap[key]]
        sorted_items = sorted(newHashMap.items(), key=lambda x: int(x[0])) 
        i = [v for _, v in sorted_items] 
        i.insert(0, so)
        return i
    
    def displayTableTwo(self, orders: List[List[str]]) -> List[List[str]]:
        table_orders = {}
        food_items = set()
        for order in orders:
            customer, table, food = order
            if table not in table_orders:
                table_orders[table] = {}
            table_orders[table][food] = table_orders[table].get(food, 0) + 1
            food_items.add(food)
        
        food_items = sorted(food_items)    
        sorted_tables = sorted(table_orders.keys(),key=int) 

        res = [['Table'] + food_items]
        for table in sorted_tables:
            table_row = [table]
            for food in food_items:
                table_row.append(str(table_orders[table].get(food,0)))
        return res
         
    

result = Solution()
result.displayTableTwo(orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]])