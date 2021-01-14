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

#perintah untuk memilih data
sql = "SELECT * FROM customers"

#mengeksekusi query
cursor.execute(sql)

#methode untuk ngambil semua data
#results = cursor.fetchall()
#methode untuk ngambil satu data
#results = cursor.fetchone()
#methode untuk ngambil satu data
results = cursor.fetchmany(1)
for data in results:
    print(data)