def sumOfThreesAndFives(inclusiveLimit: int) -> int:
    total = 0
    for number in range(0, inclusiveLimit):
        if number % 3 == 0:
            total += number
        elif number % 5 == 0:
            total += number       
    return total

print (sumOfThreesAndFives(1000));
