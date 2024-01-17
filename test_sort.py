import my_array as ma
def test_sort():
    array = ["1", "2", "3", "2", "5"]
    result1= ma.bubbleSort(array)
    result2= ma.selectionSort(array)
    excepted = array.sort()
    assert result1 == excepted
    assert result2 == excepted