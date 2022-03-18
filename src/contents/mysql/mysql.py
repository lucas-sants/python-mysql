import MySQLdb

host = "localhost"
user = "root"
password = "1234"
db = "python_db"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor(MySQLdb.cursors.DictCursor)

# ** SELECT ** 
def select(fields, tables, where=None):

	global c

	query = "SELECT " + fields + " FROM " + tables
	if (where):
		query = query + " WHERE " + where

	c.execute(query)

	return c.fetchall()

result = select("name, cpf", "students")

#print(result[0]["name"])

# ** INSERT **
def insert(values, table, fields=None):

	global c, con

	query = "INSERT INTO " + table
	if (fields):
		query = query + " (" + fields + ") "
	query =query +  " VALUES " + ",".join(["(" + v + ")" for v in values])

	c.execute(query)
	con.commit()

#values = [
#	"DEFAULT, 'Fulano Detal', '12345678911'",
#	"DEFAULT, 'Beltrano Detal', '12345678910'"]

#insert(values, "students")
#print(select("*","students"))

# ** UPDATE **
def update(sets, table, where=None):

	global c, con
	query = "UPDATE " + table
	query = query + " SET " + ",".join([field + " = '" + value + "'" for field, value in sets.items()])
	if(where):
		query = query + " WHERE " + where

	c.execute(query)
	con.commit()

# update({"name":"Ciclano Detal", "cpf":"12345678912"}, "students", "id_student = 1")
# print(select("*", "students", "id_student = 1"))

# ** DELETE ** 
def delete(table, where):

	global c, con

	query = "DELETE FROM " + table + " WHERE " + where

	c.execute(query)
	con.commit()

print(select("*", "students", "id_student = 1"))
print(delete("students","id_student = 1"))
print(select("*", "students", "id_student = 1"))
