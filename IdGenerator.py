def GenerateId(list):
    idevi = [item.id for item in list]
    cnt=1
    while True:
        if (cnt not in idevi):
            return cnt
        cnt+=1
