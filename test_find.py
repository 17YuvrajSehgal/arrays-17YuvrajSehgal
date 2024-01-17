import my_array as ma
def test_find():
    array = ["1", "2", "2"]
    item = "2"
    result= ma.findIndex(array, item)
    assert result == array.index(item)

def test_find2():
    array = ["1", "2", "2"]
    item = "0"
    result= ma.findIndex(array, item)
    assert result == -1
