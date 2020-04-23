import mysql.connector

def connectdatabase():
    mydb = mysql.connector.connect(
    host="localhost",
    user="bill",
    passwd="pass",
    database="mydatabase")
   
    return mydb

