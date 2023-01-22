import tkinter as tk
from Workout import Workout
from Exercise import Exercise
from IdGenerator import GenerateIdWorkout,GenerateIdExercise
from tkcalendar import DateEntry
from datetime import datetime
from time import strptime
workouts=[]



def ReturnWorkoutsToMain():
    someWorkouts=[]
    for workout in workouts:
        someWorkouts.append(workout)
    workouts.clear()
    return someWorkouts
def CreateExercise(args,workout,workout_window,exercise=None):
    if exercise==None:
        newExercise = Exercise(id=GenerateIdExercise(),parentId=workout.id,type=args["Type"])
        if("Name" in args):
            newExercise.name=args["Name"]
        if("Quantity" in args):
            newExercise.quantity=args["Quantity"]
        if("Weight" in args):
            newExercise.weight=args["Weight"]
        if("Intensity" in args):
            newExercise.intensity=args["Intensity"]
        if("Distance" in args):
            newExercise.distance=args["Distance"]
        if(workout.listOfExercises==None):
            workout.listOfExercises=[newExercise]
        else:
            workout.listOfExercises.append(newExercise)
    else:
        if("Name" in args):
            exercise.name=args["Name"]
        if("Quantity" in args):
            exercise.quantity=args["Quantity"]
        if("Weight" in args):
            exercise.weight=args["Weight"]
        if("Intensity" in args):
            exercise.intensity=args["Intensity"]
        if("Distance" in args):
            exercise.distance=args["Distance"]
    AddWorkouts(workout,workout_window)
    globalWorkout=workout

def ValidateExercise(window=None,args=None,workout=None,workout_window=None,exercise=None):
    if (args==None or window==None or workout==None):
        return False
    for arg in args.values():
        if(arg==None or arg=='' or arg==0):
            errorLabel = tk.Label(window,text="Ispunite sva polja!",bg="red")
            errorLabel.pack()
            errorLabel.place(x=100,y=100)
            return False
    CreateExercise(args,workout,workout_window,exercise)
    window.destroy()

def ChooseExercise(workout,exercise):
    if(exercise.type==1):
        RunningWindow(workout=workout,exercise=exercise)
    if(exercise.type==2):
        CalisthenicsWindow(workout=workout,exercise=exercise)
    if(exercise.type==3):
        WeightedWindow(workout=workout,exercise=exercise)

def AddWorkouts(workout=None ,workout_window=None):
    currY=150

    if workout_window==None:
        return False
    if workout.listOfExercises!=None and len(workout.listOfExercises) != 0:
        for i in range(0,len(workout.listOfExercises),1):
            color="white"
            if workout.listOfExercises[i].type==1:
                color="green"
            if workout.listOfExercises[i].type==2:
                color="blue"
            if workout.listOfExercises[i].type==3:
                color="red"
            distanceLabel = tk.Button(workout_window,text=workout.listOfExercises[i].name,bg=color,command=lambda j=i:ChooseExercise(workout,workout.listOfExercises[j]))
            distanceLabel.pack()
            distanceLabel.place(x=15,y=currY+20)
            currY+=30

def NewExercise(workout,workout_window):
    exercise_window = tk.Toplevel()
    exercise_window.title("Dodaj trening")
    exercise_window.geometry("600x400")

    running = tk.Button(exercise_window,text="Trcanje",width="15",height="2",bg="green",command=lambda:RunningWindow(exercise_window,workout,workout_window))
    running.place(x=15,y=15) 
    bodyweight = tk.Button(exercise_window,text="Kalisteniks",width="15",height="2",bg="blue",command=lambda:CalisthenicsWindow(exercise_window,workout,workout_window))
    bodyweight.place(x=15,y=115) 
    weighted = tk.Button(exercise_window,text="Teretana",width="15",height="2",bg="red",command=lambda:WeightedWindow(exercise_window,workout,workout_window))
    weighted.place(x=15,y=215) 

def ValidateWorkout(window=None,args=None,workout=None):
    if window==None or args==None or workout==None:
        return False
    for arg in args.values():
        if(arg==None or arg=='' or arg==0):
            errorLabel = tk.Label(window,text="Ispunite sva polja!",bg="red")
            errorLabel.pack()
            errorLabel.place(x=200,y=50)
            return False
    workout.date = args ["date"]
    workout.start = datetime.strptime(args ["start"][0:5], '%H:%M').time()
    workout.end = datetime.strptime(args ["end"][0:5], '%H:%M').time()
    window.destroy()
def OpenWorkout(workout = None):
    flag = workout==None
    if flag:
        workout= Workout(id=GenerateIdWorkout())
        workouts.append(workout)

    workout_window = tk.Toplevel()
    workout_window.title("Trening")
    workout_window.geometry("600x400")
    newExercise = tk.Button(workout_window,text="Dodaj vjezbu",width="15",height="2",bg="grey",command=lambda:NewExercise(workout,workout_window))
    newExercise.place(x=15,y=15)


    startLabel = tk.Label(workout_window,text="Pocetak treninga npr 13:30")
    startLabel.pack()
    startLabel.place(x=200,y=100)
    start = tk.Entry(workout_window)
    start.pack()
    start.place(x=200,y=125)


    
    endLabel = tk.Label(workout_window,text="Kraj treninga npr 15:00")
    endLabel.pack()
    endLabel.place(x=200,y=175)
    end = tk.Entry(workout_window)
    end.pack()
    end.place(x=200,y=200)

    date=DateEntry(workout_window,selectmode='day')
    date.grid(row=1,column=1,padx=15)

    endButton = tk.Button(workout_window,text="Kraj",width="30",height="2",bg="grey",command=lambda:ValidateWorkout(workout_window,{"date":date.get_date(),"start":start.get(),"end":end.get()},workout))
    endButton.place(x=15,y=300)


    date.place(x=15,y=100)

    if not flag:
        start.insert(0,workout.startStringTrimmed())
        end.insert(0,workout.endStringTrimmed())

    AddWorkouts(workout,workout_window)

def RunningWindow(window=None,workout=None,workout_window=None,exercise=None):
    running_window = tk.Toplevel()
    running_window.title("Dodaj trening trcanja")
    running_window.geometry("600x400")

    intensityLabel = tk.Label(running_window,text="Intenzitet trcanja")
    intensityLabel.pack()
    intensityLabel.place(x=15,y=15)
    intensity = tk.Scale(running_window, from_=0, to=10, orient=tk.HORIZONTAL)
    intensity.pack()
    intensity.place(x=15,y=40)

    distanceLabel = tk.Label(running_window,text="Koliko kilometara ste pretrcali")
    distanceLabel.pack()
    distanceLabel.place(x=15,y=100)
    distance = tk.Entry(running_window)
    distance.pack()
    distance.place(x=15,y=125) 

    if exercise!=None:
        intensity.set(exercise.intensity)
        distance.insert(0,exercise.distance)
    endButton = tk.Button(running_window,text="Kraj",width="30",height="2",bg="grey",command=lambda:ValidateExercise(running_window,{"Type":1,"Name":"Trcanje","Intensity":intensity.get(),"Distance":distance.get()},workout,workout_window,exercise))
    endButton.place(x=15,y=150)
    if window!=None:
        window.destroy()

def CalisthenicsWindow(window=None,workout=None,workout_window=None,exercise=None):
    running_window = tk.Toplevel() 
    running_window.title("Dodaj trening kalisteniksa")
    running_window.geometry("600x400")

    exercises = [
    "Sklekovi",
    "Zgibovi",
    "Cucnjevi"]
    exerciseVar = tk.StringVar(running_window)
    exerciseVar.set(exercises[0])

    exerciseDropdown = tk.OptionMenu(running_window, exerciseVar, *exercises)
    exerciseDropdown.pack()
    exerciseDropdown.place(x=15,y=15)


    quantityLabel = tk.Label(running_window,text="Broj ponavljanja")
    quantityLabel.pack()
    quantityLabel.place(x=15,y=45)
    quantity = tk.Entry(running_window)
    quantity.pack()
    quantity.place(x=15,y=80)

    if exercise!=None:
        exerciseVar.set(exercise.name)
        quantity.insert(0,exercise.quantity)

    endButton = tk.Button(running_window,text="Kraj",width="30",height="2",bg="grey",command=lambda:ValidateExercise(running_window,{"Type":2,"Name":exerciseVar.get(),"Quantity":quantity.get()},workout,workout_window,exercise))
    endButton.place(x=15,y=110)
    if window!=None:
        window.destroy()

def WeightedWindow(window=None,workout=None,workout_window=None,exercise=None):
    running_window = tk.Toplevel()
    running_window.title("Dodaj trening s utezima")
    running_window.geometry("600x400")

    exercises = [
    "Bench",
    "Deadlift",
    "Curl"]
    exerciseVar = tk.StringVar(running_window)
    exerciseVar.set(exercises[0])

    exerciseDropdown = tk.OptionMenu(running_window, exerciseVar, *exercises)
    exerciseDropdown.pack()
    exerciseDropdown.place(x=15,y=15)
    quantityLabel = tk.Label(running_window,text="Broj ponavljanja")
    quantityLabel.pack()
    quantityLabel.place(x=15,y=45)
    quantity = tk.Entry(running_window)
    quantity.pack()
    quantity.place(x=15,y=80)

    weightLabel = tk.Label(running_window,text="Sa kojom tezinom ste radili")
    weightLabel.pack()
    weightLabel.place(x=15,y=125)     
    weight = tk.Entry(running_window)
    weight.pack()
    weight.place(x=15,y=160)
    
    if exercise!=None:
        exerciseVar.set(exercise.name)
        quantity.insert(0,exercise.quantity)
        weight.insert(0,exercise.weight)

    endButton = tk.Button(running_window,text="Kraj",width="30",height="2",bg="grey",command=lambda:ValidateExercise(running_window,{"Type":3,"Name":exerciseVar.get(),"Quantity":quantity.get(),"Weight":weight.get()},workout,workout_window,exercise))
    endButton.place(x=15,y=200)
    if window!=None:
        window.destroy()

