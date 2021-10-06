lis1 = [1,2,3,4]
lis2 = lis1
#lis2 points to the same lsit object as lis1

lis2 = lis1[0:3]
#lis2 points to a new list object derived from lis1[0:3]

lis2= lis1[:]
#lis2 points to new list object derived from all of lis1

#there is also list.copy() which will provide a new list object