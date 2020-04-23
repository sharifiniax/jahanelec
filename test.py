import numpy as np
import pandas as pd
import database as db
import glob 
from pandas import read_excel
# find your sheet name at the bottom left of your excel file and assign 
# it to my_sheet 

my_sheet = '20-Transistors (BJT) - Arrays-1' # change it to your sheet name
file_name = '/home/mksh/Documents/py/data/BJT.xlsx' # change it to the name of your excel file
files=glob.glob("/home/mksh/Documents/py/data/*.xlsx")
for i in files:
    df = read_excel(i)
    column=df.columns
#print(column)
    mydb=db.connectdatabase()
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM feature")
    result=mycursor.fetchall()
    print(np.shape(result))
    print(type(result))
#print(result)
#mycursor.execute("DROP TABLE feature")
#mycursor.execute("CREATE TABLE feature (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255))")
#print(result[:][:])
#result=list(result)
    col2=[]
    try:
        col1,col2=zip(*result)
    except:
        pass
#print(col2)


    for x in column:
        if col2==None:
            sql = "INSERT INTO feature (name) VALUES (%s)"
            mycursor.execute(sql, (x,))
        if x not in col2:
            sql = "INSERT INTO feature (name) VALUES (%s)"
            mycursor.execute(sql, (x,))
        
    mydb.commit()
    mycursor.execute("SELECT * FROM feature")        
    result=mycursor.fetchall()
mydb=db.connectdatabase()
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM feature")
result=mycursor.fetchall()
col1,col2=zip(*result)
print(col2)


