from main import two_sum

def test_two_sum_one():
    nums = [2, 7, 11, 15]
    target = 9

    assert two_sum(nums, target) == [0, 1]
    
def test_two_sum_two():
    nums = [3,2,4]
    target = 6

    assert two_sum(nums, target) == [1, 2]


def test_two_sum_three():
    nums = [3, 4, 7, 11, 9, 12, 3, 4, 25]
    target = 28

    assert two_sum(nums, target) == [6, 8]