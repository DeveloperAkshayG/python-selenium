a=[13,4,5,6]

def add_element_to_list(a,b):
    a.append(b)
    return len(a)

def remove_element(a,b):
    a.remove(b)
    return len(a)

def test_total_element():
    assert add_element_to_list(a,"hi") == 5

def test_remove_element():
    assert remove_element(a,"hi") == 4

def test_update_list():
    assert add_element_to_list(a,"13") == 7 , "length is not correct"
