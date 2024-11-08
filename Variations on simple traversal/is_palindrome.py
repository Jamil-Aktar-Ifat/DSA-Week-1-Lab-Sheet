def is_pali(x):
  i = 0
  j = len(x) - 1
  while i < j:
    first = x[i]
    last = x[j]
    if first != last:
      return False
    i += 1
    j -= 1
  return True
    
    

s = "step on no pets"
print(is_pali(s), "should be True")
