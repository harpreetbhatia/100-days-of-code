import pytest


def pos_neg(a, b, negative):
  if (negative == True):
    if (a < 0 and b < 0):
      return True
  else:
    if ((a < 0 and b >= 0) or (a >= 0 and b < 0)):
      return True
  return False



def test_answer():
  assert pos_neg(1, -1, False) == True
  assert pos_neg(-1, 1, False) == True
  assert pos_neg(-4, -5, True) == True
  assert pos_neg(-4, -5, False) == False
  assert pos_neg(-4, 5, False) == True
  assert pos_neg(-4, 5, True) == False
  assert pos_neg(1, 1, False) == False
  assert pos_neg(-1, -1, False) == False
  assert pos_neg(1, -1, True) == False
  assert pos_neg(-1, 1, True) == False
  assert pos_neg(1, 1, True) == False
  assert pos_neg(-1, -1, True) == True
  assert pos_neg(5, -5, False) == True
  assert pos_neg(-6, 6, False) == True
  assert pos_neg(-5, -6, False) == False
  assert pos_neg(-2, -1, False) == False
  assert pos_neg(1, 2, False) == False
  assert pos_neg(-5, 6, True) == False
  assert pos_neg(-5, -5, True) == True

