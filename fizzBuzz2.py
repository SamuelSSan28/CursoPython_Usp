def fizzbuzz(val):
    '''
    :param val : int
    :return:  int or str
    '''
    if val % 3 == 0 and val % 5 == 0:
        return "FizzBuzz"
    elif val%5 == 0:
        return "Buzz"
    elif val % 3 == 0:
       return "Fizz"
    else:
        return val


def test_fizzBuzz1():
    assert fizzbuzz(3) == "Fizz"

def test_fizzBuzz2():
    assert fizzbuzz(15) == "FizzBuzz"

def test_fizzBuzz3():
    assert fizzbuzz(10) == "Buzz"

def test_fizzBuzz4():
    assert fizzbuzz(9) == "Fizz"

def test_fizzBuzz5():
    assert fizzbuzz(4) == 4
