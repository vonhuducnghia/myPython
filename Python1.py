a= 'how do you know'
b= a.split('d')
c= a.partition('d')
print(b)
print(c)

from decimal import*
getcontext().prec=30
d= Decimal(22)/7
print(d)
print(type(d))

e= 15/4
print(e)
f= 'I\'m begineer'
h= ''
print(h)
print(f)

g= '%s %s'
t= g %('c','cc')
print(t)

print('Welcome to Visual Studio Code')