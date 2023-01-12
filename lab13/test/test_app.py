from app import bubblesort
def test_islist():
    got = bubblesort(3)
    want = None
    assert got == want

def test_sort1():
    got = bubblesort([6, 4, 3, 1, 2])
    want = [1, 2, 3, 4, 6]
    assert got == want

def test_sort2():
    got = bubblesort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    want = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert got == want