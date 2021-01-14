#membuat koneksi ke mysql
import mysql.connector

#membuat koneksi dengan memanggil fungsi connect() dan parameter host, user dan passwd
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

#objek cursor untuk mengeksekusi perintah SQL atau query
cursor = db.cursor()

#mengeksekusi query
cursor.execute("CREATE DATABASE toko_mainan")

#mengecek status kondisi
print("Database berhasil dibuat!")