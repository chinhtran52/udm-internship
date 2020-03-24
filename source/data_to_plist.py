pose1 = './points/pose1.dat'

def readLines(file_path):
    with open(file_path) as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        return [x.strip() for x in content]

def convertToList(lines):
    result = []
    for i in lines:
        if i!='-inf  -inf  -inf':
            result.append(list(map(float, i.split())))
    return result

def generatePoints(file_path):
    lines = readLines(file_path)
    points = convertToList(lines)
    return points