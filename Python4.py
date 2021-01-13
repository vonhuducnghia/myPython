chuoi= 'String'
print(chuoi)
print(type(chuoi))
print(type('# Đây là comment'))

print('I\'m new')
s= '''line1
line2
line3'''
print(s)

v= 'line4\nline5\nline6'
print(v)

print('Wel\bcome')
print('a')

a= 68
b= '68'
print(type(a))
print(type(b))

print('35\53ni34')

#Chuỗi trần, bỏ qua Escape Sequence | r'nội dung chuỗi'
c= r'\neu mot ngay nao do'
print(c)

#Toán tử + với chuỗi
chuoi1= 'Guten'
chuoi1 += ' Tag' #chuoi1= chuoi1 + ' Tag'
print(chuoi1)

chuoi2= 'Hello'
chuoi3= ' Python'
chuoi4= chuoi2 + chuoi3
print(chuoi4)

#Toán tử in (Boolean)
print('a' in 'abc')
print('ac' in 'abc')

#Indexing và cắt chuỗi
chuoi5= 'abc xyz'
print(chuoi5[len(chuoi5)-1]) #truy cập phần tử cuối cùng của chuỗi <chuỗi>.[len(chuỗi)-1] hoặc <chuỗi>.[-1]
print(chuoi5[0:4]) #Cắt chuỗi <chuỗi>.[start:end]
print(chuoi5[1:None]) #Cắt từ [start:đến hết chuỗi] hoặc [start:]
print(chuoi5[4:])
print(chuoi5[:])
print(chuoi5[0:None:2]) #<chuỗi>.[start:end:step] | step default: 1
print(chuoi5[6:2:-2])
print(chuoi5[5::-1])
print(chuoi5[len(chuoi5):])

#Ép kiểu dữ liệu
str1= '211001'
print(type(str1))
str2= int(str1)		#int.(<giá trị>)
print(type(str2))

str3= 3.5
str4= int(str3) 	#int bỏ đi phần thập phân (không làm tròn)
print(str4)

str5= '3.5'
str6= float(str5)	#float.(<giá trị>)
print(str6)
print(type(str5))
print(type(str6))

#Thay đổi nội dung chuỗi
chuoi6= 'k' + chuoi5[1:]	#Không thể thay thế trực tiếp bằng Indexing
print(chuoi6)
print(hash(chuoi6))

str7 = '' + '' + '' + '' + '' + '' + '' + '' + ''
print(str7)