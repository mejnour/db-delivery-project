import mysql.connector

mydb = mysql.connector.connect(
    host="remotemysql.com",
    user="SKdTbdX8lK",
    passwd="yODtLD4Q0z",
    database="SKdTbdX8lK"
)

print(mydb)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Comida ORDER BY Preco ASC")

print(mycursor)
for x in mycursor:
    print(x[0])
