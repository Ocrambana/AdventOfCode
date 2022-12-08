
def strToRange(s):
    split = s.split('-')
    return [int(split[0]),int(split[1])]

def isFullyContained(r1,r2):
    firstContains = (r2[0] >= r1[0] and r1[1] >= r2[1])
    secondContains = (r1[0] >= r2[0] and r2[1] >= r1[1]) 
    return firstContains or secondContains

def overlap(r1,r2):
    return  (r1[0] <= r2[0] and r1[1] >= r2[0]) or \
            (r1[0] <= r2[1] and r1[1] >= r2[1]) or \
            (r2[0] <= r1[0] and r2[1] >= r1[0]) or \
            (r2[0] <= r1[1] and r2[1] >= r1[1])

if __name__ == '__main__':
    print("day 4")
    with open(r"../data/input-4.txt","r") as data:
        totalFC = 0
        totalOverlaps = 0
        for line in data:
            pair = line.removesuffix('\n').split(',')
            r1 = strToRange(pair[0])
            r2 = strToRange(pair[1])
            doesOverlap = overlap(r1,r2)

            print("Ranges: " +str(r1) + " " + str(r2) + "\n\tDoes Overlap? " + str(doesOverlap))
            if doesOverlap:
                totalOverlaps = totalOverlaps + 1

        print("Total ranges that totalOverlaps: " + str(totalOverlaps))
