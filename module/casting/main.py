# CASTING = MARUBAH DARI SATU TIPE KE TIPE LAIN

print("===INTEGER===")
data_int = 1
print("data =", data_int, ",type = ",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai int = 0
print("data =", data_float, ",type = ",type(data_float))
print("data =", data_str, ",type = ",type(data_str))
print("data =", data_bool, ",type = ",type(data_bool))

print("===STRING===")
data_str = "10"
print("data =", data_str, ",type = ",type(data_str))

data_int = int(data_str) # nilai string harus number = "9", karna kalo tidak akan invalid literal, example: "ucup"
data_float = float(data_str)
data_bool = bool(data_str) # jika ingin false berikan string kosong saja, example: ""
print("data =", data_int, ",type = ",type(data_int))
print("data =", data_float, ",type = ",type(data_float))
print("data =", data_bool, ",type = ",type(data_bool))


print("===FLOAT===")
data_float = 9.9
print("data =", data_float, ",type = ",type(data_float))

data_int = int(data_float) # dibulatkan, jadi tidak menjadi 10 ketika integer 
data_str = str(data_float)
data_bool = bool(data_float) # jika ingin false berikan string kosong saja, example: ""
print("data =", data_int, ",type = ",type(data_int))
print("data =", data_str, ",type = ",type(data_str))
print("data =", data_bool, ",type = ",type(data_bool))


print("===BOOLEAN===")
data_bool = False
print("data =", data_bool, ",type = ",type(data_bool))

data_int = int(data_bool) 
data_str = str(data_bool)
data_float = float(data_bool)
print("data =", data_int, ",type = ",type(data_int))
print("data =", data_str, ",type = ",type(data_str))
print("data =", data_float, ",type = ",type(data_float))
