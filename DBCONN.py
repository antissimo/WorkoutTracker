import pypyodbc as odbc


from Workout import Workout
from Exercise import Exercise
from datetime import datetime
from time import strptime

def AddZeroes(integer):
    if (integer==0):
        return "00"
    else:
        return str(integer)

def WorkoutToString(workout):
        id=str(workout.id)
        date=workout.DateString()
        start=AddZeroes(workout.start.hour)+":"+AddZeroes(workout.start.minute)+":"+AddZeroes(workout.start.second)
        end=AddZeroes(workout.end.hour)+":"+AddZeroes(workout.end.minute)+":"+AddZeroes(workout.end.second)
        return f"{id} {date} {start} {end}\n"
def NullChecker(element):
    if (element==None):
        return "None"
    return element

def ExerciseToString(exercise):
    id=str(exercise.id)
    parentId=str(exercise.parentId)
    type=str(exercise.type)
    name=str(NullChecker(exercise.name))
    quantity=str(NullChecker(exercise.quantity))
    weight=str(NullChecker(exercise.weight))
    distance=str(NullChecker(exercise.distance))
    intensity=str(NullChecker(exercise.intensity))
    return f"{id} {parentId} {type} {name} {quantity}  {weight} {distance} {intensity}\n"
def SaveStateRepository(workouts):
    if workouts==None:
        return 1
    WorkoutFile= open("Workouts.txt", "w")
    ExercisesFile= open("Exercises.txt","w")

    for workout in workouts:
        WorkoutFile.write(WorkoutToString(workout))        
        for exercise in workout.listOfExercises:
            ExercisesFile.write(ExerciseToString(exercise))
    WorkoutFile.close()
def ReverseNullChecker(element):
    if element=="None":
        return None
    return element
def ReverseNullCheckerInt(element):
    if element=="None":
        return None
    return int(element)
def CreateWorkout(line):
    arr = line.split()
    newWorkout = Workout(int(arr[0]))
    newWorkout.date=datetime(int(arr[1][0:4]),int(arr[1][5:7]),int(arr[1][8:10]))
    newWorkout.start=datetime.strptime(arr[2][0:8], '%H:%M:%S').time()
    newWorkout.end=datetime.strptime(arr[3][0:8], '%H:%M:%S').time()
    return newWorkout
def CreateExercise(line):
    arr=line.split()
    newExercise = Exercise(int(arr[0]),int(arr[1]),int(arr[2]))
    newExercise.name=ReverseNullChecker(arr[3])
    newExercise.quantity=ReverseNullCheckerInt(arr[4])
    newExercise.weight=ReverseNullCheckerInt(arr[4])
    newExercise.distance=ReverseNullCheckerInt(arr[4])
    newExercise.intensity=ReverseNullCheckerInt(arr[4])
    return newExercise
def MatchExerciseWithWorkout(exercise,workouts):
    if exercise==None or workouts==None:
        print("Error")
        return 1
    for workout in workouts:
        if exercise.parentId==workout.id:
            if(workout.listOfExercises==None):
                workout.listOfExercises=[exercise]
            else:
                workout.listOfExercises.append(exercise)
def GetWorkoutsRepository(workouts=None):
    workouts=[]
    WorkoutFile= open("Workouts.txt", "r")
    ExercisesFile= open("Exercises.txt","r")
    WorkoutLines = WorkoutFile.readlines()
    ExerciseLines= ExercisesFile.readlines()
    for workout in WorkoutLines:
        workouts.append(CreateWorkout(workout))
    for exercise in ExerciseLines:
        MatchExerciseWithWorkout(CreateExercise(exercise),workouts)
    return workouts
    