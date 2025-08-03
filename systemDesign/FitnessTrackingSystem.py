from datetime import datetime


class FitnessTrackingSystem:
    def __init__(self):
        self.users = {}
        self.user_events = {}
        
    def add_activity(self, user_id: str, activity_type: str, distance: int) -> bool:
        if user_id not in self.users:
            self.users[user_id] = {"activity_type": [activity_type], "distance": [distance]}
        else:
            if activity_type in self.users.get(user_id)["activity_type"]:   
                return False
            else:
                self.users[user_id]["activity_type"].append(activity_type)
                self.users[user_id]["distance"].append(distance)
                return True
            
            
    def update_activity(self, user_id: str, activity_type: str, distance: int) -> bool:
        if user_id not in self.users or activity_type not in self.users.get(user_id)["activity_type"]:
            return False
        for k,v in self.users.items():
            for index,value in enumerate(v["activity_type"]):
                if value == activity_type:
                    v["distance"][index] = distance
            

    def print_users(self):
        for k,v in self.users.items():
            print(f"User_Id: {k} -> Activity Type: {v["activity_type"]} Distance: {v["distance"]}km")
    
    
    def get_activity(self, user_id: str, activity_type: str) -> int | None:
        if user_id not in self.users or activity_type not in self.users.get(user_id)["activity_type"]:
            return None
        s = self.users.get(user_id)["activity_type"].index(activity_type)
        return self.users.get(user_id)["distance"][s]
    
    def activity_summary(self, user_id: str) -> dict | None:
        if user_id in self.users:
            return self.users.get(user_id)["activity_type"]
        return None
    
    def schedule_event(self, timestamp: int, user_id: str, activity_type: str, distance: int, event_time: int) -> bool:
        if user_id not in self.users or event_time <= timestamp or activity_type not in self.users.get(user_id)["activity_type"]:
            return False
       
        if user_id not in self.user_events:
            self.user_events[user_id] = {"activity_type": [activity_type], "distance": [distance], "event_time": [event_time]}
        else:
            if event_time not in self.user_events.get(user_id)["event_time"]:
                self.user_events[user_id]["activity_type"].append(activity_type)
                self.user_events[user_id]["distance"].append(distance)
                self.user_events[user_id]["event_time"].append(event_time)
        return True
        
    def get_agenda(self, user_id: str, from_time: int, to_time: int) -> list:
        if user_id not in self.users or user_id not in self.user_events:
            return False
        for k,v in self.user_events.items():
            if k == user_id:
                if v["event_time"][0] >= from_time and v["event_time"][0] <= to_time:

                    print("CHECK", k, v)
        
    

result = FitnessTrackingSystem()
result.add_activity("1", "runing", "12")
result.add_activity("1", "swimming", "33")
result.add_activity("1", "boxing", "123")
result.add_activity("1", "gym", "120")
# result.update_activity("1", "swimming", "1")
# result.get_activity("1", "swimming")
# # t = result.activity_summary("1")
result.schedule_event(13,"1","runing","30",15)
result.schedule_event(13,"1","swimming","30",19)
result.schedule_event(20,"1","swimming","30",24)
# result.schedule_event(15,"3","boxing","30",8)
# result.schedule_event(1,"3","gym","30",7)
result.get_agenda("1",14,18)

