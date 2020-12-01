from Data.user_model import User
from Data.user_model import Userstodict
from Data.user_model import Usersfromdict
import json

# import mysql.connector

# us = User(1,'admin2','1234')
# us2 = User(1,'2433','lacreta')
# users = []
# users.append(us)
# users.append(us2)
# print(Userstodict(users))
us = [{"id": 1, "username": "admin", "password": "1234"}, {"id": 2, "username": "admin2", "password": "1234"}]
us = json.dumps(us)
#print(type(json.loads(us)))
us = json.loads(us)
us =Usersfromdict(us)
print(us[1].id)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="apicourse"
# )
# bdcursor = mydb.cursor()
# query ="INSERT INTO `user` ( `user`, `password`) VALUES ('{}', '{}');".format(us.username,us.password)
# bdcursor.execute(query)
# mydb.commit()
# print(bdcursor.rowcount, "record inserted.")
# bdcursor.execute("SELECT * FROM user")

# myresult = bdcursor.fetchall()
# print(type(myresult))
# for x in myresult:
#   print(x)