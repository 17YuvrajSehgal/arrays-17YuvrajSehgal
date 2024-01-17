import my_array as ma
def test_find_sorted():
    array = ["1", "2", "2", "4"]
    item = "2"
    result= ma.findSortedArray(array, item)
    assert result == array.index(item)

def test_find_sorted2():
    array = ["1", "5", "6"]
    item = "0"
    result= ma.findSortedArray(array, item)
    assert result == -1


