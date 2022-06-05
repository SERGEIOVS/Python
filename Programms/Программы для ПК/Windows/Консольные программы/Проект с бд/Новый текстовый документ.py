import MySQLdb
conn = MySQLdb.connect('localhost','root','','test')
cursor=conn.cursor()
cursor.execute("select * from ip")
row = cursor.fetchone()
print(row)
conn.close()
