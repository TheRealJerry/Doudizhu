from fly import fei
from random import shuffle

print('Test 1: min value testing (ordered)')
print('Result: ', fei([4,4,4,5,5,5,6,7], [0,0,0,1,1,1,2,3]), '  Correct Result: True\n')
print('Test 2: max value testing (ordered)')
print('Result: ', fei([11,11,11,12,12,12,10,10,9,9], [8,8,8,7,7,7,6,6,5,5]), '  Correct Result: True\n')
print('Test 3: no prev value (ordered)')
print('Result: ', fei([11,11,11,12,12,12,10,10,9,9], None), '  Correct Result: True\n')
print('Test 4: no curr value (ordered)')
print('Result: ', fei(None, [8,8,8,7,7,7,6,6,5,5]), '  Correct Result: False\n')
print('Test 5: diff prev (ordered)')
print('Result: ', fei([8,8,8,7,7,7,6,6,5,5], [1,2]), '  Correct Result: False\n')
print('Test 6: diff curr (ordered)')
print('Result: ', fei([1,2], [8,8,8,7,7,7,6,6,5,5]), '  Correct Result: False\n')
print('Test 7: min value tesing (unordered)')
curr , prev = [4,4,4,5,5,5,6,6,7,7],[0,0,0,1,1,1,2,2,3,3]
shuffle(curr)
shuffle(prev)
print('Result: ', fei(curr, prev), '  Correct Result: True\n')
print('Test 8: max value tesing (unordered)')
min1, min2 = [11,11,11,12,12,12,10,10,9,9], [8,8,8,7,7,7,6,6,5,5]
shuffle(min1)
shuffle(min2)
print('Result: ', fei(min1, min2), '  Correct Result: True\n')

