import my_array as ma
def test_delete_at():
    array = ["1", "2", "2"]
    index = 1
    result = ma.deleteAt(array, index)
    excepted = array.pop(index)
    assert result == excepted

def test_delete_at2():
    array = ["1", "2", "2"]
    index = 3
    result = ma.deleteAt(array, index)
    excepted = array.pop()
    assert result == excepted

def test_delete_at3():
    array = ["1", "2", "2"]
    index = -1
    result = ma.deleteAt(array, index)
    excepted = array.pop()
    assert result == excepted
