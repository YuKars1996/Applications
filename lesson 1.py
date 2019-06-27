import jupyter
import chardet

a = 'разработка'
b = 'сокет'
c = 'декоратор'

a_b = a.encode()
b_b = b.encode()
c_b = c.encode()

print(a_b, b_b, c_b, sep='\n')

a_s = a_b.decode('utf-8')
b_s = b_b.decode('latin1')
c_s = c_b.decode('utf-16')

print(a_s, b_s, c_s, sep='\n')