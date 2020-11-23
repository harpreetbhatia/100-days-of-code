import pytest

def has22(nums):
  for i in range(len(nums) -1):
    if (nums[i] == 2 and nums[i+1] == 2):
      return True
  return False
      
def test_answer():
  assert has22([1, 2, 2]) == True
  assert has22([1, 2, 1, 2]) == False
  assert has22([2, 1, 2]) == False
  assert has22([2, 2, 1, 2]) == True
  assert has22([1, 3, 2]) == False
  assert has22([1, 3, 2, 2]) == True
  assert has22([2, 3, 2, 2]) == True
  assert has22([4, 2, 4, 2, 2, 5]) == True
  assert has22([1, 2]) == False
  assert has22([2, 2]) == True
  assert has22([2]) == False
  assert has22([]) == False
  assert has22([3, 3, 2, 2]) == True
  assert has22([5, 2, 5, 2]) == False

