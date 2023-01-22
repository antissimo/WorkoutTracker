import tkinter as tk
from frmExercise import OpenWorkout
import matplotlib.pyplot as plt
import numpy as np

buttons=[]
def ListWorkouts(workouts=None):
    if workouts==None:
        return 0
    list_window = tk.Toplevel()
    list_window.title("Lista treninga")
    list_window.geometry("600x400")
    
    SaveButton = tk.Button(list_window,text="Osvjezi",width="10",height="2",bg="blue",command=lambda:AddWorkouts(workouts,list_window))
    SaveButton.place(x=15,y=20) 
    PlotButton = tk.Button(list_window,text="Napravi graf vjezbanja",width="20",height="2",bg="blue",command=lambda:AddGraph(workouts,Plot.get()))
    PlotButton.place(x=100,y=20)
    PlotLabel = tk.Label(list_window,text="Napisite za koju godinu zelite graf (defaultno je trenutna godina)")
    PlotLabel.pack()
    PlotLabel.place(x=250,y=20)
    Plot = tk.Entry(list_window)
    Plot.pack()
    Plot.place(x=250,y=40) 
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

def GetAmountOfHours(month=None,year=None,workouts=None):
    if month==None or year==None or workouts==None:
        return 0
    cnt=0
    for workout in workouts:
        if workout.date.year==year and workout.date.month==month:
            cnt+=int(workout.IntLength())
    return cnt



def AddGraph(workouts=None,year=None):
    fig,ax = plt.subplots()
    if year==None or year=='':
        year=2023
    else:
        year=int(year)
    fruits = ['JAN', 'FEB', 'MAR', 'APR','MAY', 'JUN', 'JUL', 'AUG','SEP', 'OCT', 'NOV', 'DEC']
    counts = [GetAmountOfHours(i,year,workouts) for i in range(1,13,1)]
    ax.set_title(f"Graf vjezbanja za godinu {year}.")

    ax.bar(fruits, counts, label=fruits, color='red')

    plt.show()