import pytest



def sum13(nums):
  sum = 0
  i = 0
  while i < len(nums):
    if (nums[i] == 13):
      i += 2
      continue
    sum += nums[i]
    i += 1
  return sum
 
def test_answer():
  assert sum13([1, 2, 2, 1]) == 6
  assert sum13([1, 1]) == 2
  assert sum13([1, 2, 2, 1, 13]) == 6
  assert sum13([1, 2, 13, 2, 1, 13]) == 4
  assert sum13([13, 1, 2, 13, 2, 1, 13]) == 3
  assert sum13([]) == 0
  assert sum13([13]) == 0
  assert sum13([13, 13]) == 0
  assert sum13([13, 0, 13]) == 0
  assert sum13([13, 1, 13]) == 0
  assert sum13([5, 7, 2]) == 14
  assert sum13([5, 13, 2]) == 5
  assert sum13([0]) == 0
  assert sum13([13, 0]) == 0

