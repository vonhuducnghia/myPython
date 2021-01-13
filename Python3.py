a= 22/7
print(a)
print(type(a))

from decimal import* #lấy toàn bộ nội dung thư viện Decimal
getcontext().prec= 30 #lấy tối đa 30 chữ số phần nguyên và phần thập phân
b= Decimal(22)/Decimal(7)
print(b)
print(type(b))

#Fraction
from fractions import* #lấy toàn bộ nội dung của thư viện decimal
Fraction (3, 4)
print(Fraction(3, 4))
print(Fraction)

#Complex numbers
c= complex(3, 7)
print(c)
d= 5 + 13j
print(d)
print(c.imag)

print(type(c))
print(complex(4, 1))
print(complex(6))
print(complex(0, 7))

#
print(16/3)

#import hàm
import math
print(22/7)
print(math.trunc(22/7))
print(math.floor(22/7))
print(math.ceil(22/7))
print(math.fabs(-22/7))
print(math.sqrt(22/7))
print(math.gcd(12, 18))