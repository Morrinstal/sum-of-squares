def sumOfSquares(dictionary):
    return sum(dictionary.values())

squaresDict = {i: i**2 for i in range(1, 11)}
totalSum = sumOfSquares(squaresDict)
print(f"Сумма всех квадратов: {totalSum}")