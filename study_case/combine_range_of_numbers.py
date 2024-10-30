# gabungan area rentang dari angka

# ++++++3-------10++++++

# inputUser = float(input("Masukkan angka yang bernilai\nkurang dari 3\natau\nlebih dari 10:\n"))

# # periksa angka kurang dari 3
# # +++++++3--------
# isLessThan = (inputUser < 3)
# print("kurang dari 3 = ", isLessThan)


# # periksa angak kurang dari 3
# # --------10++++++++
# isMoreThan = (inputUser > 10)
# print("lebih dari 10 = ",isMoreThan)

# # periksa menggunakan operator OR
# # ++++++3-------10++++++
# isCorrectWithOperatorOr = isLessThan or isMoreThan
# print("angka yang dimasukkan = ", isCorrectWithOperatorOr)


# # soal 2
# # ---------3++++++++++10----------

# inputUser = float(input("Masukkan angka yang bernilai\nlebih dari 3\natau\nkurang dari 10:\n"))

# # --------3++++++++
# isMoreThan = (inputUser > 3)
# print("lebih dari 3 = ", isMoreThan)


# # +++++++++10---------
# isLessThan = (inputUser < 10)
# print("kurang dari 10 = ",isLessThan)

# # --------- 3 ++++++++++ 10 ----------
# isCorrectWithOperatorAnd = isMoreThan and isLessThan
# print("angka yang dimasukkan = ", isCorrectWithOperatorAnd)


# =============================================================================================================================


# # Real SOal
# # SOAL 3

# # ------ 3 +++++++ 5 ------- 8 +++++++ 11 -------

# inputUser = float(input('Masukkan angka yang bernilai\nlebih dari 3\nkurang dari 5\nlebih dari 8\nkurang dari 11:\n'))


# # look for ------ 3 +++++++
# isMoreThanFirst = inputUser > 3
# print("lebih dari 3 =", isMoreThanFirst)

# # look for ++++++ 5 ------
# isLessThanFirst = inputUser < 5
# print("kurang dari 5 =", isLessThanFirst)

# # look for ------- 8 +++++++
# isMoreThanSecond = inputUser > 8
# print("lebih dari 8 =", isMoreThanSecond)

# # look for ++++++ 11 --------
# isLessThanSecond = inputUser < 11
# print("kurang dari 11 =", isLessThanSecond)

# isCorrectWithOperatorXor = isMoreThanFirst ^ isLessThanFirst ^ isMoreThanSecond ^ isLessThanSecond
# print("angka yg dimasukkan =", isCorrectWithOperatorXor)


# =================================================================================================================================


# # SOAL 4
# # +++++++ 0 -------- 5 ++++++++ 8 --------- 11 +++++++

# inputUser = float(input("Masukkan angka yg bernilai\nkurang dari 0\nlebih dari 5\nkurang dari 8\nlebih dari 11:\n"))

# # look for ++++++ 0 -------
# isLessThanFirst = inputUser < 0
# print("kurang dari 0 =", isLessThanFirst)


# # look for ------ 5 +++++++
# isMoreThanFirst = inputUser > 5
# print("lebih dari 5 =", isMoreThanFirst)


# # look for ++++++++ 8 --------
# isLessThanSecond = inputUser < 8
# print("kurang dari 8 =", isLessThanSecond)


# # look for -------- 11 ++++++++
# isMoreThanSecond = inputUser > 11
# print("lebih dari 11 =", isMoreThanSecond)


# isCorrectWithOperatorXor = isLessThanFirst ^ isMoreThanFirst ^ isLessThanSecond ^ isMoreThanSecond
# print("angka yg dimasukkan =", isCorrectWithOperatorXor)


# # SOAL 5
print("cara yg pertama")
inputUser = float(input("masukkan nilai:"))

plus1 = inputUser > 0 and inputUser <  5
print(plus1)

plus2 = inputUser > 8 and inputUser <  11
print(plus2)

print(10*'+')

answer = plus1 or plus2
print(answer)


# SOAL 4
print("cara yg kedua")
inputUser = float(input("masukkan nilai:"))

plus1 = inputUser < 0 or inputUser >  5
print(plus1)

plus2 = inputUser < 8 or inputUser >  11
print(plus2)

print(10*'+')

answer = plus1 and plus2
print(answer)
