import pytest


def love6(a, b):
  return (a == 6 or \
          b == 6 or \
          a + b == 6 or \
          abs(a - b) == 6)


def test_answer():
  assert love6(6, 4) == True
  assert love6(4, 5) == False
  assert love6(1, 5) == True
  assert love6(1, 6) == True
  assert love6(1, 8) == False
  assert love6(1, 7) == True
  assert love6(7, 5) == False
  assert love6(8, 2) == True
  assert love6(6, 6) == True
  assert love6(-6, 2) == False
  assert love6(-4, -10) == True
  assert love6(-7, 1) == False
  assert love6(7, -1) == True
  assert love6(-6, 12) == True
  assert love6(-2, -4) == False
  assert love6(7, 1) == True
  assert love6(0, 9) == False
  assert love6(8, 3) == False
  assert love6(3, 3) == True
  assert love6(3, 4) == False

