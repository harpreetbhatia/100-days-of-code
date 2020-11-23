import pytest

def sum2(nums):
  if len(nums) < 1:
    return 0
  elif len(nums) < 2:
    return nums[0]
  else:
    return nums[0] + nums[1]

def test_answer():
  assert sum2([1, 2, 3]) == 3
  assert sum2([1, 1]) == 2
  assert sum2([1, 1, 1, 1]) == 2
  assert sum2([1, 2]) == 3
  assert sum2([1]) == 1
  assert sum2([]) == 0
  assert sum2([4, 5, 6]) == 9
  assert sum2([4]) == 4

