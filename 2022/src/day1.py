
if __name__ == '__main__':
    print("day 1")
    caloriesStack = [2,1,0]
    actualCalories = 0
    with open(r"../data/1-input.txt","r") as fileData:
        flag = True
        while flag:
            line = fileData.readline()

            if line in ['\n','']:
                if actualCalories > caloriesStack[0]:
                    caloriesStack[2] = caloriesStack[1]
                    caloriesStack[1] = caloriesStack[0]
                    caloriesStack[0] = actualCalories
                elif actualCalories > caloriesStack[1]:
                    caloriesStack[2] = caloriesStack[1]
                    caloriesStack[1] = actualCalories
                elif actualCalories > caloriesStack[2]:
                    caloriesStack[2] = actualCalories
                actualCalories = 0
                flag = line != ''
            else :
                actualCalories = actualCalories + int(line)
    
    max3Sum = 0
    for i in range(3):
        actual = caloriesStack.pop();
        print("\tAdding " + str(actual))
        max3Sum = max3Sum + actual;

    print("Max calories carried " + str(max3Sum))

    