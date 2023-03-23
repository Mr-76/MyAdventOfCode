bigger = 0;
number = 0
with open("elvesCalories.txt",'r') as file:
    for line in file:
        if (line == '\n'):
            #print("jump elf")
            if (number >= bigger):
                bigger = number
                number = 0
            else:
                number = 0
        else:
            number += int(line.strip())
    else:
        print(bigger)

