
from sqlite3 import*
connection=sqlite3.connect("test.db")
cursor=connection.cursor()#adds cursor -what you use to interact with database


cursor.execute("""create table IF NOT EXISTS testone 
(one integer
,two text
,three text
,four text
)""")#inside are columns/categorys

#inserting data into database
cursor.execute("INSERT INTO testone VALUES ('1','steve','bob','jeff')")


connection.commit()#pushes changes into database

cursor.execute("SELECT*FROM testone")#selects a table in database
results=cursor.fetchall()#selects everything within that table
print(results)
connection.close()
