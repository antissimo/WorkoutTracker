def GenerateIdWorkout():
    WorkoutFileRead= open("WorkoutId.txt", "r")
    id = int(WorkoutFileRead.read())+1
    WorkoutFileRead.close()
    WorkoutFileWrite = open("WorkoutId.txt", "w")
    WorkoutFileWrite.write(str(id))
    WorkoutFileWrite.close()
    return id
def GenerateIdExercise():
    ExerciseFileRead= open("ExerciseId.txt", "r")
    id = int(ExerciseFileRead.read())+1
    ExerciseFileRead.close()
    ExerciseFileWrite = open("ExerciseId.txt", "w")
    ExerciseFileWrite.write(str(id))
    ExerciseFileWrite.close()
    return id

