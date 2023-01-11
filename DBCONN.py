import pypyodbc as odbc


from Workout import Workout
from datetime import datetime
from time import strptime

def AddZeroes(integer):
    if (integer==0):
        return "00"
    else:
        return str(integer)

def SaveStateRepository(workouts):
    
    driver = 'SQL SERVER'
    server ='DESKTOP-58RHK6B\SQLEXPRESS'
    database = 'WorkoutTracker'

    connectionString = f"""
        DRIVER={{{driver}}};
        SERVER={server};
        DATABASE={database};
        Trust_Connection=yes;
    """
    connection = odbc.connect(connectionString)
    cursor = connection.cursor()
    cursor.execute('DELETE FROM dbo.workouts')
    for i in workouts:
        id=i.id
        date=workouts[i].DateString()
        start=AddZeroes(i.start.hour)+":"+AddZeroes(i.start.minute)+":"+AddZeroes(i.start.second)
        end=AddZeroes(i.end.hour)+":"+AddZeroes(i.end.minute)+":"+AddZeroes(i.end.second)
        query=f"INSERT INTO dbo.workouts values({str(id)},'{date}','{start}','{end}')"

        cursor.execute(query)
    cursor.close()
    del cursor
    

def GetWorkoutsRepository(workouts=None):
    workouts=[]
    driver = 'SQL Server'
    server ='DESKTOP-58RHK6B\SQLEXPRESS'
    database = 'WorkoutTracker'

    connectionString = f"""
        Driver={{{driver}}};
        Server={server};
        DATABASE={database};
        Trust_Connection=yes;
    """
    try:
        connection = odbc.connect(connectionString)
    except Exception as e:
        print(e)
        return 0
    cursor = connection.cursor()


    try:
        cursor.execute('SELECT * FROM dbo.Workouts')
    except Exception as e:
        print(e)


    for i in cursor:
        id = i[0]
        date =  datetime.strptime(i[1], '%Y-%d-%m').date()
        start = datetime.strptime(i[2][0:8], '%H:%M:%S').time()
        end = datetime.strptime(i[3][0:8], '%H:%M:%S').time()
        newWorkout = Workout(id=id,date=date,start=start,end=end)   
        workouts.append(newWorkout)
    cursor.execute('SELECT * FROM dbo.Exercises')
    ## Napravi da se doda po parentIdu u workouts u listu exercisea svakon objektu
     
    
    