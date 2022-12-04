mappingPoints = {
    'A': {
        'Z' : 2,
        'Y' : 1,
        'X' : 3
    },
    'B': {
        'Z' : 3,
        'Y' : 2,
        'X' : 1
    },
    'C': {
        'Z' : 1,
        'Y' : 3,
        'X' : 2
    }
}

if __name__ == '__main__':
    print("day 2")
    totalPoints = 0
    with open(r"../data/2-input.txt","r") as data:
        for line in data:
            s = line[0:3].split(' ')
            actual = 0
            if s[1] == 'Z': # win
                actual = actual + 6
            elif s[1] == 'Y': # draw
                actual = actual + 3
            
            actual = actual + mappingPoints[s[0]][s[1]]
            totalPoints = totalPoints + actual
    print(str(totalPoints))
