# Input: menerima satu bilangan bulat n
n = int(input("Bilangan: "))

# Proses: mengalikan n dengan 1 sampai 10
# Kondisi berhenti: perulangan berhenti setelah i mencapai 10
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Output: menampilkan hasil perkalian n x 1 sampai n x 10