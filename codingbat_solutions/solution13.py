import pytest


def alarm_clock(day, vacation):
  if (vacation == True):
    if (0 < day < 6):
      return "10:00"
    else:
      return "off"
  else:
    if (0 < day < 6):
      return "7:00"
    else:
      return "10:00"
  return "off"


def test_answer():
  assert alarm_clock(1, False) == '7:00'
  assert alarm_clock(5, False) == '7:00'
  assert alarm_clock(0, False) == '10:00'
  assert alarm_clock(6, False) == '10:00'
  assert alarm_clock(0, True) == 'off'
  assert alarm_clock(6, True) == 'off'
  assert alarm_clock(1, True) == '10:00'
  assert alarm_clock(3, True) == '10:00'
  assert alarm_clock(5, True) == '10:00'

