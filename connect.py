#membuat koneksi ke mysql
import mysql.connector

#membuat koneksi dengan memanggil fungsi connect() dan parameter host, user dan passwd
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

#mengecek status kondisi
if db.is_connected():
    print("Berhasil terhubung ke database.")