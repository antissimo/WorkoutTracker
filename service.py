from DBCONN import SaveStateRepository,GetWorkoutsRepository
def SaveState(workouts):
    SaveStateRepository(workouts)


def GetWorkouts():
    return GetWorkoutsRepository()