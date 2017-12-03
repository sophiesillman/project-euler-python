startingNumber = 2*3*5*7*11*13*17*19*2

def testForModulus(testedNumber: int)-> bool:
    flag = True
    for number in range(1, 20):
        if testedNumber % number != 0:
            flag = False
            break
    return flag

while (True):
    if testForModulus(startingNumber) == False:
        startingNumber += 20
    else:
        print(startingNumber)
        break
