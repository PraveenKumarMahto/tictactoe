from flask_restful import Resource,request
from validators.move import validator
from dao.move import create_move_instance
from views import move as moveview

class Move(Resource):
    def post(self):
        payload = request.json
        if not validator(payload):
            return {"response" : "move instance bad Response"}

        create_move_instance(
                payload["game_instance_id"],
                payload["move"],
                payload["player"],
                
                ) 
        return moveview.single(payload)