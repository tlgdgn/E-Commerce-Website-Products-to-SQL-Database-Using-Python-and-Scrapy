import mysql.connector
import json

with open('petlebi_products.json',encoding="utf-8") as json_file:
    data = json.load(json_file)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password"
)

mycursor = mydb.cursor()
#mycursor.execute("SET NAMES 'utf8'")
#mycursor.execute('SET CHARACTER SET utf8')
#mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
mycursor.execute("USE mydatabase")
#mycursor.execute("ALTER DATABASE mydatabase CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
#mycursor.execute("CREATE TABLE IF NOT EXISTS petlebi (URL longtext, name longtext, price longtext, barcode longtext, image longtext, brand longtext, category longtext, sku longtext, product_ID longtext)")
for record in data:
    sql = f"INSERT INTO petlebi (URL, name, price, barcode, image, brand, category, sku,product_ID) \n VALUES ('{record['URL']}', '{record['name']}', '{record['price']}' , '{record['barcode']}' , '{record['image']}', '{record['brand']}' ,'{record['category']}' , '{record['sku']}' , '{record['product ID']}' );"
    mycursor.execute(sql)

mydb.commit()
mydb.close()