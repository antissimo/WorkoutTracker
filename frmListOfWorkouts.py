import tkinter as tk
from frmExercise import OpenWorkout
import matplotlib
matplotlib.use('TkAgg')

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import ( FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

buttons=[]
def ListWorkouts(workouts=None):
    if workouts==None:
        return 0
    list_window = tk.Toplevel()
    list_window.title("Lista treninga")
    list_window.geometry("600x400")
    
    SaveButton = tk.Button(list_window,text="Osvjezi",width="10",height="2",bg="blue",command=lambda:AddWorkouts(workouts,list_window))
    SaveButton.place(x=15,y=20) 
    PlotButton = tk.Button(list_window,text="Napravi graf vjezbanja",width="20",height="2",bg="blue",command=lambda:AddGraph(workouts))
    PlotButton.place(x=100,y=20)
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
def AddGraph(workouts=None):
    if workouts==None :
        return 0
    plot_window = tk.Toplevel()
    plot_window.title("Graf treninga")
    plot_window.geometry("900x600")

    f = Figure(figsize=(5, 4), dpi=100)
    a = f.add_subplot(111)
    t = arange(1, 12, 1)
    s = sin(2*pi*t)
    f.suptitle('Graf za 2022. godinu', fontsize=16)

    a.plot(t, s) 
    canvas = FigureCanvasTkAgg(f, master=plot_window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, plot_window)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)