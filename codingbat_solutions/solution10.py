import pytest

def cigar_party(cigars, is_weekend):
  if (is_weekend and cigars >=40):
    return True
  if (cigars >= 40 and cigars <= 60):
    return True
  return False
  
def test_answer():
  assert cigar_party(30, False) == False
  assert cigar_party(50, False) == True
  assert cigar_party(70, True) == True
  assert cigar_party(30, True) == False
  assert cigar_party(50, True) == True
  assert cigar_party(60, False) == True
  assert cigar_party(61, False) == False
  assert cigar_party(40, False) == True
  assert cigar_party(39, False) == False
  assert cigar_party(40, True) == True
  assert cigar_party(39, True) == False

