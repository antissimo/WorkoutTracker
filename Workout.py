from datetime import datetime
from time import strptime

class Workout:
    def __init__(self,id,date=None,start=None,end=None,listOfExercises=None):
        self.id=id
        self.date=date
        self.start=start
        self.end=end
        self.listOfExercises=listOfExercises
    def DateString(self):
        #dateString =  datetime.strptime(str(self.date), '%Y-%d-%m').date()
        return f"{self.date.year}-{self.date.month}-{self.date.day}"
    def startString(self):
        return str(self.start)
    def endString(self):
        return str(self.end)
    def IntLength(self):
        differenceInMinutes=(self.end.hour*60+self.end.minute) - (self.start.hour*60+self.start.minute)
        len = differenceInMinutes/60
        return len


    def LengthOfWorkout(self):
        differenceInMinutes=(self.end.hour*60+self.end.minute) - (self.start.hour*60+self.start.minute)
        len = f"{differenceInMinutes//60}:{differenceInMinutes%60}"
        return len
    def startStringTrimmed(self):
        return str(self.start)[0:5]
    def endStringTrimmed(self):
        return str(self.end)[0:5]

    
