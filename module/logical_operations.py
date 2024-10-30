#  not , or, and, xor

# NOT 

print("====NOT====")
a = False 
c = not a 
print('data a =', a)
print('--------------- NOT')
print('data c =', c)


# OR -> jika salah satunya true, maka hasilnya adalah true

print("====OR====")
a = False 
b = False 
c = True 
d = a or b or c
print(a, 'OR', b, 'OR', c, '=', d)
a = False 
b = True 
c = a or b 
print(a, 'OR', b, '=', c)
a = True 
b = False 
c = a or b 
print(a, 'OR', b, '=', c)
a = True 
b = True 
c = a or b 
print(a, 'OR', b, '=', c)

# AND -> jika dua buah nilai true, maka hasil true

print("=======AND=======")
a = False 
b = True 
c = True
d = a and b and c
print(a, 'and', b, 'and', c, '=', d)
a = False 
b = True 
c = a and b 
print(a, 'and', b, '=', c)
a = True 
b = False 
c = a and b 
print(a, 'and', b, '=', c)
a = True 
b = True 
c = a and b 
print(a, 'and', b, '=', c)

# XOR -> akan true jika salah satunya true, sisanya false

print("=======XOR=======")
a = False 
b = False 
c = a ^ b 
print(a, 'XOR', b, '=', c)
a = False 
b = True 
c = a ^ b 
print(a, 'XOR', b, '=', c)
a = True 
b = False 
c = a ^ b 
print(a, 'XOR', b, '=', c)
a = True 
b = True 
c = a ^ b 
print(a, 'XOR', b, '=', c)
