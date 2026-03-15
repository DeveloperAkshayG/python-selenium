def add_two_numbers(a,b):
    return a+b

def test_add_small_numbers():
    assert add_two_numbers(1,3) == 4

def test_add_large_numbers():
    assert add_two_numbers(100,300) == 400

def test_two_number():
    assert add_two_numbers(-5,5) == 10, "The addition result should be zero"