import array as array
set1 = {'Blue','Green'}
set2 = {'Blue','Yellow'}

print('Set 1 is', set1)
print('Set 2 is', set2)

symdif = str(set1.symmetric_difference(set2))
print('The symmertric difference of Set 1 and Set 2 is',symdif)

set1 = {1,2,3,4,5}
set2 = {1,5,6,7,8,9}

print(set1)
print(set2)

symdif = str(set1.symmetric_difference(set2))
print('The symmertric difference of Set 1 and Set 2 is',symdif)