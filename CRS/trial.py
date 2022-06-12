import re
import MySQLdb
import string

connec = MySQLdb.connect("localhost","root","","iplmdatabase")
cursor = connec.cursor()

a = cursor.execute("SELECT LAST_INSERT_ID() from crs_shifterapplicant;")
a = int(a)
select = "SELECT department from crs_shifterapplicant where id = %(ss)s"
b = cursor.execute(select,{'ss':a})
b = cursor.fetchone()
b = str(b)
b = re.sub(r"[^a-zA-Z0-9]","",b)
print(b)
search = "SELECT id from crs_department where courseName = %(s)s"
Course = cursor.execute(search,{'s':b})
Course = cursor.fetchone()
Course = str(Course)
Course = re.sub(r"[^a-zA-Z0-9]","",Course)
print(Course)