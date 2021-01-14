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

#perintah untuk mengupdate data
sql = "UPDATE customers SET name=%s, address=%s WHERE customer_id=%s"
values = [
    ("Galih", "Depok", 2),
    ("Fani", "Bandung", 3),
    ("Doni", "Jakarta", 4),
    ("Ella", "Surabaya", 5)
]

for val in values:
    #mengeksekusi query
    cursor.execute(sql, val)
    #untuk menyimpan data
    db.commit()

#mengecek status kondisi
print("{} data diubah".format(len(values)))