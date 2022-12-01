def check_same(a, b):
  a=a.lower()
  b=b.lower()
  if a==b:
      return 'same'
  return 'false'
      
print(check_same('Hello', 'HeLLo'))
