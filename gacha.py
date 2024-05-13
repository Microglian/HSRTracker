'''
Gacha tab has a header and three columns based on priority:
High     Medium      Low

Each task within a column is something to pull.
A task is either a Character task or a Lightcone task.
'''

class Gacha():
    def __init__(self) -> None:
        self.tasks = []
        
        
class GachaTask():
    def __init__(self, uuid, priority, pos, object, target) -> None:
        self.uuid = uuid
        self.priority = priority
        self.pos = pos
        self.object = object
        self.target = target
        
        
        