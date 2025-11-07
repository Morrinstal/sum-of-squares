from sumOfSquares import sumOfSquares

def test_sum_of_squares_basic():
    squaresDict = {i: i**2 for i in range(1, 11)}
    assert sumOfSquares(squaresDict) == 385

def test_sum_of_squares_empty():
    assert sumOfSquares({}) == 0
