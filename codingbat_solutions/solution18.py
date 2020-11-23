import pytest
Medium python string problems -- 1 loop.. Use + to combine strings, len(str) is the number of chars in a String, str[i:j] extracts the substring starting at index i and running up to but not including index j.


def double_char(str):
  double_char_str = ""
  for i in range(len(str)):
    double_char_str += (str[i] + str[i])
  return double_char_str

def test_answer():
  assert double_char('The') == 'TThhee'
  assert double_char('AAbb') == 'AAAAbbbb'
  assert double_char('Hi-There') == 'HHii--TThheerree'
  assert double_char('Word!') == 'WWoorrdd!!'
  assert double_char('!!') == '!!!!'
  assert double_char('') == ''
  assert double_char('a') == 'aa'
  assert double_char('.') == '..'
  assert double_char('aa') == 'aaaa'

