
import mysql.connector

#starting conection
mydb = mysql.connector.connect(
  host="remotemysql.com",
  user="SKdTbdX8lK",
  passwd="yODtLD4Q0z"
)

print(mydb)