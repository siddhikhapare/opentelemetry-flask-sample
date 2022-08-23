import pymysql.cursors
#import json
from flask import jsonify,request

class user_model():
    def __init__(self):
        try:
           self.connection = pymysql.connect(host='localhost',
                            user='root',
                            password='password',
                            database='usersapi')
                            #cursorclass=pymysql.cursors.DictCursor)	
            self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
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
        self.cursor.execute("SELECT * FROM users")
        result = self.cursor.fetchall()
        response = jsonify(result)
        return response
   
    def createUser_model(self,data):
        try:
            _json = request.json
            _name = _json['name']
            _email = _json['email']
            #_password = _json['password']
           
            if _name and _email and request.method == 'POST':
                sqlQuery = "INSERT INTO users(name, email) VALUES(%s, %s)"
                data = (_name, _email)            
                self.cursor.execute(sqlQuery, data)
                self.connection.commit()
                return 'Users created successfully'
            else:
                return 'not found page'
                
        except Exception as e:
            print(e)

    def deleteUsers_model(self,id):
        try:
            self.cursor.execute(f"DELETE FROM users WHERE id={id}")
            self.connection.commit()
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

