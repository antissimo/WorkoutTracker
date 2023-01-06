import tkinter as tk
from frmExercise import OpenWorkout 


def MainWindow():

    window = tk.Tk()
    window.title("Aplikacija za pracenje vjezbanja")
    window.geometry("900x600")
    WorkoutButton = tk.Button(window,text="Dodaj trening",width="30",height="2",bg="grey",command=lambda:OpenWorkout())
    WorkoutButton.place(x=15,y=290) 
    window.mainloop()

MainWindow()

