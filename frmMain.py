import tkinter as tk
from frmExercise import OpenWorkout,workouts
from service import SaveState,GetWorkouts
from frmListOfWorkouts import ListWorkouts


def MainWindow():

    window = tk.Tk()
    window.title("Aplikacija za pracenje vjezbanja")
    window.geometry("900x600")


    WorkoutButton = tk.Button(window,text="Dodaj trening",width="30",height="2",bg="grey",command=lambda:OpenWorkout())
    WorkoutButton.place(x=15,y=15) 

    WorkoutButton = tk.Button(window,text="Ispisi treninge",width="30",height="2",bg="grey",command=lambda:ListWorkouts(workouts))
    WorkoutButton.place(x=15,y=300) 

    SaveButton = tk.Button(window,text="Spremi",width="10",height="2",bg="grey",command=lambda:SaveState(workouts))
    SaveButton.place(x=300,y=15) 

    GetButton = tk.Button(window,text="Dohvati",width="10",height="2",bg="grey",command=lambda:GetWorkouts())
    GetButton.place(x=300,y=300) 



    window.mainloop()

MainWindow()

