from DBCONN import SaveStateRepository,GetWorkoutsRepository,DeleteAllRepository
def SaveState(workouts):
    SaveStateRepository(workouts)


def GetWorkouts():
    return GetWorkoutsRepository()

def DeleteAll(window):
    return DeleteAllRepository(window)