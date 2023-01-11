from enum import Enum

# class syntax
class TypeOfWorkout(Enum):
    Running = 1
    Calisthenics= 2
    Weighted = 3

class Exercise:
     def __init__(self,id,parentId,type,name=None,quantity=None,weight=None,distance=None,intensity=None):
      self.id=id
      self.parentId=parentId
      self.type=type
      self.name=name
      self.quantity=quantity
      self.weight=weight
      self.distance=distance
      self.intensity=intensity
        