import MySQLdb
conn = MySQLdb.connect('/dbfolder','root','','testdb')
cursor=conn.cursor()
cursor.execute("select * from ip")
row = cursor.fetchone()
print(row)
conn.close()
