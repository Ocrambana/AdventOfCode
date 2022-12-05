
def getPriority(c):
    if c.isupper():
       return ord(c) - 38
    else:
        return ord(c) - 96

if __name__ == '__main__':
    print("day 3")
    totalPriority = 0
    with open(r"../data/3-input.txt","r") as data:
        flag = True
        one = data.readline()
        two = data.readline()
        three = data.readline()

        while flag:
            for c in one:
                ind = two.find(c)
                if ind >= 0:
                    if three.find(c) >= 0:
                        totalPriority = totalPriority + getPriority(c)
                        break

            one = data.readline()
            two = data.readline()
            three = data.readline()

            flag = one != "" and two != "" and three != ""

    print("Total sum of priorities " + str(totalPriority))