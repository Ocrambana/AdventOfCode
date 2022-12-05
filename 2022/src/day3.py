
def getPriority(c):
    if c.isupper():
       return ord(c) - 38
    else:
        return ord(c) - 96

if __name__ == '__main__':
    print("day 3")
    totalPriority = 0
    with open(r"../data/3-input.txt","r") as data:
        for line in data:
            halfLength = int((len(line) - 1) * 0.5)
            sac1 = line[0:halfLength]
            sac2 = line[halfLength:]

            print(line +" -> " + sac1 +" + " + sac2)
            for c in sac1:
                if sac2.find(c) >= 0:
                    totalPriority = totalPriority + getPriority(c)
                    print("Same element " + c + " priority " + str(getPriority(c)))
                    break

    print("Total sum of priorities " + str(totalPriority))