import random

NUMS = []

def SEARCHING_ALGORITHM():
    FOUND = False
    LOWERPART = 0
    UPPERPART = len(NUMS) - 1
    COUNT = 0
    LENGTH = random.randint(1, 5000)

    for i in range(LENGTH):
        rnum = random.randint(0, 5000)
        NUMS.append(rnum)

    NUMS = list(dict.fromkeys(NUMS))
    NUMS.sort()
    print(NUMS)

    VALUE = int(input('>> '))
    while FOUND == False:
        MID = int((LOWERPART + UPPERPART)) / 2
        MID = round(MID)
        if NUMS[MID] == VALUE:
            print(f'Found At Array Index {MID)
            FOUND = True

        if NUMS[MID] > VALUE:
            UPPERPART -= 1; 
            COUNT += 1
        else:
           LOWERPART += 1
           COUNT += 1

        if COUNT > len(NUMS) * 2:
            print(f'Value Not Found in Array')
            break

SEARCHING_ALGORITHM()
