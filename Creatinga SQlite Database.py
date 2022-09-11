import sqlite3#three quotation marks because three lines ONLY DO  THIS ONCE SO PUT IT IN SEPERATE FILE WHICH CREATES DATABASE THEN HAVE YOUR MAIN FILE INSERT INTO IT
connection=sqlite3.connect("test.db")
cursor=connection.cursor()#adds cursor -what you use to interact with database

cursor.execute("""create table testone
(one integer
,two text
,three text
,four text
)""")#inside are columns/categorys
