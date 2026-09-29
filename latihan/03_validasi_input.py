# Input: menerima nilai ujian dari 0-100
nilai = float(input("Nilai 0-100: "))

# Proses: memeriksa apakah nilai berada di luar rentang 0-100
# kondisi berhenti: perulangan berhenti jika nilai berada dalam rentang 0-100
while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = float(input("Nilai 0-100: "))

# Output: menampilkan nilai yang sudah valid
print(f"Nilai diterima: {nilai}")