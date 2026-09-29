# Input: menerima bilangan bulat positif n
n = int(input("n: "))

# Proses: menjumlahkan bilangan dari 1 sampai n
# Kondisi berhenti: perulangan berhenti setelah i mencapai n
total = 0
for i in range(1, n + 1):
    total += i

# Output: menampilkan hasil jumlah 1 sampai n
print(f"Jumlah = {total}")