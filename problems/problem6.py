def SumOfSquares(limit: int)-> int:
    total = 0
    for number in range(1, limit + 1):
        total += number*number
    return total
       
def SquareOfSum(limit: int)->int:
    total=0
    for number in range(1, limit + 1):
        total += number
    return total * total

print (SquareOfSum(100) - SumOfSquares(100))
