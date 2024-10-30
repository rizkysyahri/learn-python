# konversi celcius ke satuan lain

# celcius = float(input('Masukan suhu dalam celcius: ' ))
# print("suhu adalah", celcius, "Celcius")

# reamur = (4/5) * celcius
# print("suhu dalam reamur adalah", reamur, "Reamur")

# fahrenheit = ((9/5) * celcius) + 32
# print("suhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")

# kelvin = celcius + 273
# print("suhu dalam kelvin adalah", kelvin, "Kelvin")


# konversi fahrenheit ke kelvin

fahrenheit = float(input('Masukan suhu dalam fahrenheit: ')) 
kelvin = ((fahrenheit - 32) * 5/9) + 273                            # K = (F - 32) x 5/9 + 273 
print("suhu dalam kelvin adalah", kelvin)                                              

# konversi kelvin ke fahrenheit

kelvin = float(input('Masukkan suhu dalam kelvin: '))
fahrenheit = ((kelvin - 273) * 9/5) + 32                            # F = (K - 273) x 9/5 + 32
print("suhu dalam fahrenheit adalah", fahrenheit)




