def IsPalindrome(number: int) -> bool:
    return str(number) == str(number)[::-1]

listOfNumbers = []

for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        if IsPalindrome(x * y):
            listOfNumbers.append(x * y)

print (max(listOfNumbers))
