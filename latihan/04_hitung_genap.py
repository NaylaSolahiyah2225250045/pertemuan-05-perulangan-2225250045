# Input: menerima bilangan bulat positif n
n = int(input("n: "))

# Proses: menghitung banyak bilangan genap dari 1 sampai n
jumlah_genap = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        jumlah_genap += 1

# Output: menampilkan banyak bilangan genap
print(f"Banyak bilangan genap = {jumlah_genap}")