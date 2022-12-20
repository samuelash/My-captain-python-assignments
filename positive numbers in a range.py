list1=[12,-7,5,64,-14]
list2=[12,14,-95,3]
print('\nthe original list1 is:',list1)
print('\nthe original list2 is:',list2)

for i in list1:
    if i<0:
        list1.remove(i)
print('\nlist only with positive numbers:\n',list1)
for x in list2:
    if x<0:
        list2.remove(x)
print('\nlist only with positive numbers:\n',list2)
        
