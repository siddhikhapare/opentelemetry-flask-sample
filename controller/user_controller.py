from app import app
from flask import request
#from http import HTTPStatus
# classname and filename should be same as java file
from model.user_model import user_model
obj = user_model()

@app.route('/users/getall')
def getusers():
    return obj.getusers_model()

@app.route('/create',methods=['POST'])
def createusers():
    return obj.createUser_model(request.form)

@app.route('/user/<id>')
def getuserdetails(id):
    return obj.userdetails_model(id)

@app.route('/delete/<id>',methods=['DELETE'])
def deleteusers(id):
    return obj.deleteUsers_model(id)


# @app.errorhandler(404)
# def page_not_found(e):    
#     return not_found(data=str(e), status_code=404)

# @app.errorhandler(HTTPStatus.NOT_FOUND)
# def page_not_found(e):
#     return obj.not_found(message=str(e), status_code=HTTPStatus.NOT_FOUND)