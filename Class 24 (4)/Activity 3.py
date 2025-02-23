#Arrays
import array as arr
a = arr.array('b',[1,2,3,4,3,5,3,6,3,7])
print(str(a))

print('The number of occurence of 3 in the array is :')
coun = str(a.count(3))
print(coun)

print('The reverse of the array is :')
a.reverse()
print(str(a))