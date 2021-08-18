f = [x for x in range(1, 10)]
print(f)

"""
it will works as same as, Its a oneliner

for i in range(0,10):
  print(i)
"""
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)

"""
['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7']
"""
