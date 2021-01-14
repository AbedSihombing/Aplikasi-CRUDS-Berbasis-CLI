#membuat koneksi ke mysql
import mysql.connector

#membuat koneksi dengan memanggil fungsi connect() dan parameter host, user dan passwd
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_mainan"
)

#objek cursor untuk mengeksekusi perintah SQL atau query
cursor = db.cursor()

#perintah untuk menginsert data
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
values = [
    ("Doni", "Jakarta"),
    ("Ella", "Surabaya"),
    ("Fani", "Bandung"),
    ("Galih", "Depok")
]

for val in values:
    #mengeksekusi query
    cursor.execute(sql, val)
    #untuk menyimpan data
    db.commit()

#mengecek status kondisi
print("{} data ditambahkan".format(len(values)))