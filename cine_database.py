import mysql.connector

class MyDatabase:
    def open_connection(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="db_cine")
        return connection
    
    def insert_db(self,PELICULA,HORA,FECHA,IDIOMA):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_cartelera(PELICULA,HORA,FECHA,IDIOMA) VALUES(%s,%s,%s,%s)"
        data = (PELICULA, HORA, FECHA,IDIOMA)
        cursor.execute(query, data)
        my_connection.commin()
        my_connection.close()

