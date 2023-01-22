def GenerateIdWorkout():
    WorkoutFileRead= open("WorkoutId.txt", "r")
    content = WorkoutFileRead.read()
    if content == '':
        id = 0
    else:
        id = int(content)+1
    WorkoutFileRead.close()
    WorkoutFileWrite = open("WorkoutId.txt", "w")
    WorkoutFileWrite.write(str(id))
    WorkoutFileWrite.close()
    return id
def GenerateIdExercise():
    ExerciseFileRead= open("ExerciseId.txt", "r")
    content = ExerciseFileRead.read()
    if content == '':
        id = 0
    else:
        id = int(content)+1
    ExerciseFileRead.close()
    ExerciseFileWrite = open("ExerciseId.txt", "w")
    ExerciseFileWrite.write(str(id))
    ExerciseFileWrite.close()
    return id

