def FibonacciFinder(limit: int) -> list:
    fibonacci = [1,1]
    while fibonacci[-1] + fibonacci[-2] < limit:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

def SumEvenListItems(listOfNumbers: list) -> int:
    total = 0
    for number in listOfNumbers:
        if number % 2 == 0:
            total += number
    return total

print (SumEvenListItems(FibonacciFinder(4000000)))
    
    
    
