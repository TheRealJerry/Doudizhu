from fly import check_4_card
from random import shuffle
print('Test 1: 4+pairs (ordered)')
print(check_4_card([8,8,8,8,4,4,5,5], [5,5,5,5,6,6,7,7]), 'Correct Result: True\n')
print('Test 2: 4+1 (ordered)')
print(check_4_card([12,12,12,12,11,10], [10,10,10,10,9,8]), 'Correct Result: True\n')
print('Test 3: No prev value + curr is 4+pair(ordered)')
print(check_4_card([12,12,12,12,11,11], []), 'Correct Result: True\n')
print('Test 3: No prev value (ordered)')
print(check_4_card([], [12,12,12,12,11,11]), 'Correct Result: False\n')
print('Test 5: diff prev (ordered)')
print(check_4_card([12,12,12,12,11,10], [10,10,9,9,8,8]), 'Correct Result: False\n')
print('Test 6: diff curr (ordered)')
print(check_4_card([10,10,9,9,8,8], [12,12,12,11,10]), 'Correct Result: False\n')
print('Test 7: min value tesing (unordered)')
curr , prev = [1,1,1,1,2,2,3,3], [0,0,0,0,1,1,2,2]
shuffle(curr)
shuffle(prev)
print(check_4_card(curr, prev), '  Correct Result: True\n')
print('Test 8: Max value (unordered)')
curr , prev = [12,12,12,12,11,11,10,10],[11,11,11,11,10,10,10,10]
shuffle(curr)
shuffle(prev)
print(check_4_card(curr, prev), '  Correct Result: True\n')
