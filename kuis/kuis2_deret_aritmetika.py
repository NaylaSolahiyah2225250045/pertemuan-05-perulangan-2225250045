print("Deret Aritmetika")

# Input: menerima suku pertama a, beda d, dan banyak suku n
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

# Proses: memastikan n merupakan bilangan positif
# Kondisi berhenti: perulangan berhenti saat n > 0
while n <= 0:
    print("Banyak suku harus positif.")
    n = int(input("Banyak suku n: "))

# Proses: menghitung dan menjumlahkan setiap suku
total = 0
for i in range(n):
    suku = a + i * d
    total += suku
    print(f"Suku {i + 1} = {suku:.2f}")

# Output: menampilkan jumlah seluruh suku
print(f"Jumlah = {total:.2f}")