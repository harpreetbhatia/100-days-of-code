import pytest

def sleep_in(weekday, vacation):
  if weekday==False and vacation==False:
    return True
  if weekday==True and vacation==False:
    return False
  if weekday==False and vacation==True:
    return True
  if weekday==True and vacation==True:
    return True
  return False


def test_answer():
  assert sleep_in(False, False) == True
  assert sleep_in(True, False) == False
  assert sleep_in(False, True) == True
  assert sleep_in(True, True) == True

