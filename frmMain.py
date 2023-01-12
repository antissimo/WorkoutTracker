import tkinter as tk
from frmExercise import OpenWorkout,workouts,ReturnWorkoutsToMain
from service import SaveState,GetWorkouts
from frmListOfWorkouts import ListWorkouts
mainWorkouts=[]

def IdPresent(id):
    for workout in mainWorkouts:
        if workout.id==id:
            return 1
    return 0

def UpdateWorkouts():
    for workout in GetWorkouts():
        if not IdPresent(workout.id):
            mainWorkouts.append(workout)
    return 0
def UpdateWorkoutsNew():
    for workout in ReturnWorkoutsToMain():
        if not IdPresent(workout.id):
            mainWorkouts.append(workout)
    return 0

def ListWorkoutsMain():
    UpdateWorkoutsNew()
    ListWorkouts(mainWorkouts)
    return 0
def SaveStateMain():
    SaveState(mainWorkouts)
    return 0
def MainWindow():

    window = tk.Tk()
    window.title("Aplikacija za pracenje vjezbanja")
    window.geometry("900x600") 

    WorkoutButton = tk.Button(window,text="Dodaj trening",width="30",height="2",bg="grey",command=lambda:OpenWorkout())
    WorkoutButton.place(x=15,y=15) 

    WorkoutButton2 = tk.Button(window,text="Ispisi treninge",width="30",height="2",bg="grey",command=lambda:ListWorkoutsMain())
    WorkoutButton2.place(x=15,y=300) 

    SaveButton = tk.Button(window,text="Spremi",width="10",height="2",bg="grey",command=lambda:SaveStateMain())
    SaveButton.place(x=300,y=15) 

    GetButton = tk.Button(window,text="Dohvati",width="10",height="2",bg="grey",command=lambda:UpdateWorkouts())
    GetButton.place(x=300,y=300) 



    window.mainloop()

MainWindow()

