import pymysql
# First create a database
#Connect here with the database created
con=pymysql.connect(host="localhost",user="root",password="",db="crud")

curser=con.cursor()

#curser.execute("insert into record(id,name) values('1','Paco');")
#curser.execute("insert into record(id,name) values('2','Jose');")
#print("Data inserted in the Database")

#curser.execute("update record set name='Juan' where id='2'")
#print("Updated!")

#curser.execute("delete from record where name='Juan'")
#print("Deleted")

# For fetching data
curser.execute("select * from record")
print(curser.fetchall())

con.commit()
con.close()



