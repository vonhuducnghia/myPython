# List in Python [], seperate elements by , list contains all types of data

list1 = ['Nghia', 19, 2001.00]
print(list1)

list2 = [i for i in range(30)]
print(list2)

list3 = [[x, x*1, x*3] for x in range(1,4)]
print(list3)

list4 = list('1')   # list(iterable; strings; copy list to different memory location)
list4a = list(list4)
list4a += ['Melissa']
print(list4)
print(list4a)

list5 = [1, 2, 'N', 'M', [3, 4]]
b = 2 in list5
c = list5[-1][-2]   # indexing list
d = list5[::-1] # backward
print(c)
print(d)

list6 = [1, 1, 1, 4, 5, 7]
cntlst = list6.count(1)     # <listname>.count(element) count the quantity of the element in that list
indexlst = list6.index(1)   # <listname>.index(element) return the location of that element, return error if no element found
copylst = list6.copy()      # <listname>.copy() duplicate that list without changing or modifying the original list
print(cntlst)
print(indexlst)