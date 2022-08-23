from app import app
from flask import request
from model.user_model import user_model
obj = user_model()

@app.route('/users/getall')
def getusers():
    return obj.getusers_model()

@app.route('/create',methods=['POST'])
def createusers():
    return obj.createUser_model(request.form)

@app.route('/delete/<id>',methods=['DELETE'])
def deleteusers(id):
    return obj.deleteUsers_model(id)

