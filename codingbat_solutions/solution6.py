import pytest


def first_last6(nums):
  return (nums[0] == 6 or nums[-1] == 6)

def test_answer():
  assert first_last6([1, 2, 6]) == True
  assert first_last6([6, 1, 2, 3]) == True
  assert first_last6([13, 6, 1, 2, 3]) == False
  assert first_last6([13, 6, 1, 2, 6]) == True
  assert first_last6([3, 2, 1]) == False
  assert first_last6([3, 6, 1]) == False
  assert first_last6([3, 6]) == True
  assert first_last6([6]) == True
  assert first_last6([3]) == False
  assert first_last6([5, 6]) == True
  assert first_last6([5, 5]) == False
  assert first_last6([1, 2, 3, 4, 6]) == True
  assert first_last6([1, 2, 3, 4]) == False

