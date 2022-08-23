# import pymysql
#from flaskext.mysql import MySQL
# from db import mysql
#from urllib import response
import pymysql.cursors
#import json
# from flask import make_response,jsonify
from flask import jsonify,request

class user_model():
    def __init__(self):
        try:
            #conncetion establishment code
            #cursor = None

            # conn = mysql.connect()
            # cursor = conn.cursor(pymysql.cursors.DictCursor)
            #we are assigning global scope variables are connection and cursor
            #cursor will help to execute query and integrate/interact wit db 
            self.connection = pymysql.connect(host='localhost',
                            user='root',
                            password='redhat12',
                            database='usersapi')
                            #cursorclass=pymysql.cursors.DictCursor)	
            self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
            #self.cursor = self.connection.cursorclass()
            # rows = self.cursor.fetchall()
            # resp = jsonify(rows)
            self.connection.commit()
            #self.connection.autocommit=True
            print("connection established")
        except Exception as e:
            print(e)
            #print("Some error")
        #finally:
            #self.cursor.close() 
            #self.connection.close()  

    def getusers_model(self):
        #business logic-
        #query execution code
        self.cursor.execute("SELECT * FROM users")
        result = self.cursor.fetchall()
        response = jsonify(result)
        return response
        #print(response)
        #return json.dumps(result)
        #print(result)
        # if len(result)>0:
        #     return json.dumps(result)
        # else:
        #     return " No data found"


    def createUser_model(self,data):
        try:
            _json = request.json
            _name = _json['name']
            _email = _json['email']
            #_password = _json['password']
            # validate the received values
            if _name and _email and request.method == 'POST':
                #do not save password as a plain text
                # _hashed_password = generate_password_hash(_password)
                # save edits
                #sql = f"INSERT INTO users(name, email, password) VALUES('{data['name']}','{data['email']}','{data['password']}')"
                #data = (_name, _email, _password,)
                #result = self.cursor.execute(sql,data)
                #self.cursor.execute(f"INSERT INTO users(name, email, password) VALUES('{data['name']}','{data['email']}','{data['password']}')")
                #resp = jsonify(result)
                sqlQuery = "INSERT INTO users(name, email) VALUES(%s, %s)"
                data = (_name, _email)            
                self.cursor.execute(sqlQuery, data)
                self.connection.commit()
                return 'Users created successfully'
            else:
                return 'not found page'
                #return not_found(self,message=str(e),status_code=HTTPStatus.NOT_FOUND)
        except Exception as e:
            print(e)

    def deleteUsers_model(self,id):
        try:
            self.cursor.execute(f"DELETE FROM users WHERE id={id}")
            self.connection.commit()
            # resp = jsonify('User deleted successfully!')
            # return resp
            return 'User deleted successfully!'
        except Exception as e:
            print(e)

    def userdetails_model(self,id):
        try:
            self.cursor.execute("SELECT id, name, email FROM users WHERE id =%s", id)
            userRow = self.cursor.fetchone()
            respone = jsonify(userRow)
            return(response)
        except Exception as e:
            print(e) 

    # def not_found(self,message,status_code):
    #     message = {
    #         'status': status_code,
    #         'message': 'Not Found: ' + request.url,
    #     }
    #     resp = jsonify(message)
    #     resp.status_code = status_code
    #     return resp

# def userdetails_model(self,id):
    #     try:
    #         self.cursor.execute("SELECT id, name, email FROM users WHERE id =%s", id)
    #         userRow = self.cursor.fetchone()
    #         respone = jsonify(userRow)
    #         return(response)
    #     except Exception as e:
    #         print(e)


#https://codehandbook.org/handle-404-error-python-flask/
#https://www.askpython.com/python-modules/flask/flask-error-handling
#https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/