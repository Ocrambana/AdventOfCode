
if __name__ == '__main__':
    print ("day5")
    with open("../data/5-input.txt","r") as data:
        line = data.readline()
        stacks = [[] for i in range(9)]
        while not any(chr.isdigit() for chr in line):
            line.removesuffix('\n')
            for i in range(len(line)):
                index = int(i / 4)
                if i % 4 == 1 and line[i] != ' ':
                    stacks[index].append(line[i])
            line = data.readline()

        data.readline()

        for line in data:
            line = line.removesuffix('\n')
            splits = line.split(' ')
            toMove = int(splits[1])
            start = int(splits[3]) - 1
            destination = int(splits[5]) - 1

            for i in range(toMove):
                stacks[destination].insert(i,stacks[start].pop(0))

        
        for s in stacks:
            print(s)