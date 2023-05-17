import psycopg2
import mysql





#Following function will create a mysql connection.
def mysql_connection():
    #Get your DB connection from "DataBase Info" Tab
    HOST = 'localhost'
    USERNAME = 'username'
    PASSWORD = 'password'
    DATABASE = 'database'
    

    mydb = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        password=PASSWORD,
        database=DATABASE
    )


    return mydb
