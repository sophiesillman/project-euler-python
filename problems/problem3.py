def largestPrimeFactor(numberToFactor: int)-> int:
    currentDivisorStore = 2

    while numberToFactor > currentDivisorStore:
        if numberToFactor % currentDivisorStore == 0:
            numberToFactor = numberToFactor / currentDivisorStore
            currentDivisorStore = 2
        else:
            currentDivisorStore += 1

    return currentDivisorStore
    
    
print (largestPrimeFactor(600851475143))
