from typing import List

class Potluck:
    def __init__(self):
        self.participants = {}
        self.dishes = {}
        self.votes = {}
    def add_participant(self, member_id: str) -> bool:
        if member_id in self.participants:
            return False
        val = len(self.participants)
        self.participants[member_id] = val + 1
        return True
    
    def remove_participantes(self, member_id: str) -> bool:
        if member_id in self.participants:
            del self.participants[member_id]
            return True
        return False
    
    def add_dish(self, member_id: str, dish_name: str) -> bool:
        if member_id not in self.participants or member_id in self.dishes:
            return False
        self.dishes[member_id] = dish_name
        return True

    def vote(self, member_id: str, vote_id: str) -> bool:
        if member_id not in self.participants or member_id in self.votes:
            return False

        self.votes[vote_id] = self.dishes[member_id]
       
    def dish_of_the_day(self) -> str | None: 
        ans = {}
        mostVotes = 0
        for k,v in self.votes.items():
            if v in ans:
                ans[v] += 1
                mostVotes = max(mostVotes, ans[v])
            else:
                ans[v] = 1

        if len(ans) == 0:
            return None
        so = sorted(ans.items(), key=lambda x: (x[1], x[0]), reverse=True)
        if len(ans) >= 2:
            if so[0][1] == so[1][1]:
                for index,value in self.dishes.items():
                    for d in ans.keys():
                        if d == value:
                            mostRecentParticipant = sorted(self.participants,  key=lambda  x: x[1])[0]
                            if mostRecentParticipant == index:
                                return d
            else:
                return list(ans)[0]   
            
                        
             
        

    def printParticipant(self):
        print(self.participants)
        # print(self.participants, self.dishes, self.votes)
        
        

result = Potluck()
result.add_participant("participante1")
result.add_participant("participante2")
result.add_participant("participante3")
result.add_dish("participante1", "dish1")
result.add_dish("participante2", "dish2")
result.add_dish("participante3", "dish3")
result.vote("participante1", "vote1")
# result.vote("participante2", "vote2")
result.vote("participante2", "vote3")
# result.vote("participante1", "vote4")
# result.vote("participante1", "vote5")
t = result.dish_of_the_day()
print(t)
# result.printParticipant()
