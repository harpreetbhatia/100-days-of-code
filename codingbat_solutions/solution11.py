import pytest
def date_fashion(you, date):
  if (you <= 2 or date <= 2):
    return 0
  if (you >= 8 or date >= 8):
    return 2
  return 1
    
def test_answer():
  assert date_fashion(5, 10) == 2
  assert date_fashion(5, 2) == 0
  assert date_fashion(5, 5) == 1
  assert date_fashion(3, 3) == 1
  assert date_fashion(10, 2) == 0
  assert date_fashion(2, 9) == 0
  assert date_fashion(9, 9) == 2
  assert date_fashion(10, 5) == 2
  assert date_fashion(2, 2) == 0
  assert date_fashion(3, 7) == 1
  assert date_fashion(2, 7) == 0
  assert date_fashion(6, 2) == 0

