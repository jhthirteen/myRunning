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
            classes.append(data[i][1])
    return classes