# setiap hasil dari operasi komparasi adalah boolean

# > , < ,>= , <= , == , != , is, is not

a = 4
b = 2

# lebih besar dari ( > )
print("====== lebih besar dari ( > )")
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)

# kurang dari ( < )
print("====== kurang dari ( < )")
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil)

# lebih dari sama dengan  ( >= )
print("====== lebih dari sama dengan ( >= )")
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil) # hasilnya true karena perbedaan antara lebih besar ( > ) dan lebih besar sama dengan ( >= ) adalah 
                              # yg ( > ) dihitung dimulai 3.0000001 sekian , makanya true 
                              # yg ( >= ) dihitung dimulai benar benar dari 3, ibarat 3 >= 3 = true, karna dihitung benar benar dari 3 bukan 3.0000001   


# kurang dari sama dengan  ( <= )
print("====== kurang dari sama dengan ( <= )")
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)

#  sama dengan  ( == )
print("====== sama dengan ( == )")
hasil = a == 3
print(a, '==', 3, '=', hasil)
hasil = b == 3
print(b, '==', 3, '=', hasil)
hasil = b == 2
print(b, '==', 2, '=', hasil)

# tidak sama dengan  ( != )
print("====== tidak sama dengan ( != )")
hasil = a != 3
print(a, '!=', 3, '=', hasil)
hasil = b != 3
print(b, '!=', 3, '=', hasil)
hasil = b != 2
print(b, '!=', 2, '=', hasil)

# 'is' sebagai komparasi object identify
x = 5 # this is assignment membuat object
y = 6
print('nilai x =', x ,'id = ', hex(id(x)))
print('nilai y =', y ,'id = ', hex(id(y)))

hasil = x is y
print("x is y =", hasil)

x = 5 # this is assignment membuat object
y = 6
print('nilai x =', x ,'id = ', hex(id(x)))
print('nilai y =', y ,'id = ', hex(id(y)))

hasil = x is not y
print("x is y =", hasil)
