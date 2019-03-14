from fly import check_3_card
from random import shuffle
print('Test 1: Min value (ordered)')
print(check_3_card([1,1,1,2], [0,0,0,1]), 'Correct Result: True\n')
print('Test 2: Max value (ordered)')
print(check_3_card([12,12,12,11], [11,11,11,10]), 'Correct Result: True\n')
print('Test 3: No prev value (ordered)')
print(check_3_card([12,12,12,11], None), 'Correct Result: True\n')
print('Test 3: No prev value (ordered)')
print(check_3_card(None, [12,12,12,11]), 'Correct Result: False\n')
print('Test 5: diff prev (ordered)')
print(check_3_card([12,12,12,11], [1,2]), 'Correct Result: False\n')
print('Test 6: diff curr (ordered)')
print(check_3_card([1,2], [12,12,12,11]), 'Correct Result: False\n')
print('Test 7: min value tesing (unordered)')
curr , prev = [1,1,1,2], [0,0,0,1]
shuffle(curr)
shuffle(prev)
print(check_3_card(curr, prev), '  Correct Result: True\n')
print('Test 8: Max value (unordered)')
curr , prev = [12,12,12,11],[11,11,11,10]
shuffle(curr)
shuffle(prev)
print(check_3_card(curr, prev), '  Correct Result: True\n')
