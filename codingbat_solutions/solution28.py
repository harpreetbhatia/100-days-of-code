import pytest

def sum67(nums):
  found6 = False
  sum = 0
  for num in nums:
    if (num == 6): found6 = True
    if (found6 and num == 7): 
      found6 = False
      continue
    if found6: continue
    sum += num
  return sum
  

def test_answer():
  assert sum67([1, 2, 2]) == 5
  assert sum67([1, 2, 2, 6, 99, 99, 7]) == 5
  assert sum67([1, 1, 6, 7, 2]) == 4
  assert sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]) == 2
  assert sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]) == 2
  assert sum67([2, 7, 6, 2, 6, 7, 2, 7]) == 18
  assert sum67([2, 7, 6, 2, 6, 2, 7]) == 9
  assert sum67([1, 6, 7, 7]) == 8
  assert sum67([6, 7, 1, 6, 7, 7]) == 8
  assert sum67([6, 8, 1, 6, 7]) == 0
  assert sum67([]) == 0
  assert sum67([6, 7, 11]) == 11
  assert sum67([11, 6, 7, 11]) == 22
  assert sum67([2, 2, 6, 7, 7]) == 11