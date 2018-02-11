from flask_restful import Resource
from flask import request 
from utils.constants import session_expiry_span 
from dao.user import get_user_by_mail 
from dao.session import create_user_session
from time import time
import uuid 


class UserValidation(Resource):

    def post(self):
        payload = request.json

        try:
            email = payload['email']
            password = payload['password']
        except:
            return {"response" : "Bad request"} , 400

        user = get_user_by_mail(email)
        if not user:
            return {"response" : "User does not exist"}, 404

        if not user["password"] == password:
            return {"response" : "Incorrect Password"}, 401

        token = str(uuid.uuid4())
        create_user_session( user["_id"] , token )

        return {
            "response" : {
                "token" : token,
                "expiry" : time() + session_expiry_span
            }
        }