'''
Gacha tab has a header and three columns based on priority:
High     Medium      Low

Each task within a column is something to pull.
A task is either a Character task or a Lightcone task.
'''

class Gacha():
    def __init__(self) -> None:
        self.highPriority = GachaColumn()
        self.medPriority = GachaColumn()
        self.lowPriority = GachaColumn()
        
    
    
class GachaColumn():
    def __init__(self) -> None:
      self.tasks = []  
    
    
class GachaTask():
    def __init__(self) -> None:
        pass
    

class GachaTaskChar(GachaTask):
    def __init__(self) -> None:
        pass
    
    
class GachaTaskLC(GachaTask):
    def __init__(self) -> None:
        pass