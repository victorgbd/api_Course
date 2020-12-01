from flask import Flask, request
from Data.user_model import User
from Data.user_model import Userstodict
from Data.user_model import Usersfromdict
import mysql.connector
import json

app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="apicourse"
)
bdcursor = mydb.cursor()
@app.route('/')
def a():
    return json.dumps("hola")


@app.route('/users', methods=['POST', 'GET','PUT'])
def user():
    if request.method == 'POST':
        # user = request.args.get('user', None)
        # password = request.args.get('password', None)
        us = Usersfromdict(json.loads(request.get_data()))
        query = "INSERT INTO `user` ( `user`, `password`) VALUES ('{}', '{}');".format(
            us[0].username, us[0].password)
        bdcursor.execute(query)
        mydb.commit()
        print(bdcursor.rowcount, "record inserted.")
        return json.dumps("Usuario Insertado correctamente")
    elif request.method == 'PUT':
        us = Usersfromdict(json.loads(request.get_data()))
        query = "UPDATE `user` SET `user`= '{}',`password`='{}' WHERE `id`='{}';".format(
            us[0].username, us[0].password, us[0].id)
        bdcursor.execute(query)
        mydb.commit()
        print(bdcursor.rowcount, "record updated.")
        return json.dumps("Usuario Actualizado correctamente")
    else:
        bdcursor.execute("SELECT * FROM user")
        myresult = bdcursor.fetchall()
        list_users = []
        for x in myresult:
            us = User(x[0], x[1], x[2])
            list_users.append(us)
        return json.dumps(Userstodict(list_users))

@app.route('/users/<int:id>', methods=['DELETE'])
def users(id):
    if request.method == 'DELETE':
        query = "DELETE FROM `user` WHERE `id`='{}';".format(id)
        bdcursor.execute(query)
        mydb.commit()
        print(bdcursor.rowcount, "record deleted.")
        return json.dumps("Usuario Eliminado correctamente")
        
if __name__ == "__main__":
    app.run(debug=True, port=5000)
