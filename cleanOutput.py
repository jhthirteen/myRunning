def checkIfUser(data, userInfo):
    splitPosition = userInfo.find(' ')
    username = userInfo[:splitPosition]
    password = userInfo[splitPosition+1:]
    for i in range(len(data)):
        if( username == data[i][0] and password == data[i][1]):
            return True
    return False

def findClasses(data, id):
    classes = []
    for i in range(len(data)):
        if( data[i][0] == id[0][0] ):
            numWords = 0
            splitIndexes = []
            runningIndex = 0
            classFormatted = ""
            for c in data[i][1]:
                if( c.isupper() ):
                    numWords += 1
                    splitIndexes.append(runningIndex)
                runningIndex += 1
            initial = 0
            for j in range(len(splitIndexes)):
                if( splitIndexes[j] == 0 ):
                    continue
                classFormatted = classFormatted + data[i][1][initial:splitIndexes[j]] + " "
                initial = splitIndexes[j]
            classFormatted = classFormatted + data[i][1][initial:len(data[i][1])]
            classes.append(classFormatted)

    return classes

def combineInput(login, classes):
    userPass = login.split()
    classes = [userPass[0]] + classes #adding our username as the first argument to their classlist
    return classes