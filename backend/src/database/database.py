import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="revisorprecios"  # Cambia esto al nombre de tu base de datos
)

def guardar_en_db(titulo, precio, image):
    mycursor = mydb.cursor()
    sql = "INSERT INTO productos (titulo, precio, image) VALUES (%s, %s, %s)"
    val = (titulo, precio, image)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")