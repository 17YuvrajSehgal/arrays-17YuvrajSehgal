import my_array as ma
def test_count():
    array = ["1", "2", "2"]
    result = ma.getCount(array)
    assert result == len(array)