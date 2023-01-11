import tkinter as tk
from frmExercise import OpenWorkout
buttons=[]
def ListWorkouts(workouts=None):
    if workouts==None:
        return 0
    list_window = tk.Toplevel()
    list_window.title("Lista treninga")
    list_window.geometry("600x400")
    
    SaveButton = tk.Button(list_window,text="Osvjezi",width="10",height="2",bg="blue",command=lambda:AddWorkouts(workouts,list_window))
    SaveButton.place(x=15,y=20) 
    AddWorkouts(workouts,list_window)
    
def AddWorkouts(workouts=None,window=None):
    if workouts==None or window==None:
        return 1
    for button in buttons:
        button.destroy()
    buttons.clear()
    currY=60
    for i in range(0,len(workouts),1):
        workout = tk.Button(window,text=workouts[i].DateString()+"    Trajanje: "+workouts[i].LengthOfWorkout(),bg="orange",command=lambda j=i:OpenWorkout(workouts[j]))
        workout.pack()
        workout.place(x=15,y=currY+20)
        buttons.append(workout)
        currY+=30
