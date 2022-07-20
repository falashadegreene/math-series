from series import fibonacci, lucas, sum_series

def test_fibonacci_input0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_input2():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fibonacci_input3():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_lucas_input1():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_input2():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def  test_lucas_input3():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_sum_series_input1():
    actual = sum_series(1)
    expected = 2
    assert actual == expected

def test_sum_series_input2():
    actual = sum_series(2)
    expected = 2
    assert actual == expected

def test_sum_series_input3():
    actual = sum_series(4)
    expected = 10
    assert actual == expected




