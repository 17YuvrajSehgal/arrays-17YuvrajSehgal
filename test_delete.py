import my_array as ma
def test_delete():
    array = ["1", "2", "2"]
    item = "2"
    result = ma.delete(array, item)
    array.remove(item)
    assert result == array

def test_delete2():
    array = ["1", "2", "2"]
    item = "3"
    result = ma.delete(array, item)
    assert result == -1
