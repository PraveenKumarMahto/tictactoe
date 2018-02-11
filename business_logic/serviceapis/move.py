from flask_restful import Resource,request
from validators.move import validator
from dao.move import create_move_instance, get_move_by_move_id
from views import move as moveview

class Move(Resource):
    def post(self):
        payload = request.json
        if not validator(payload):
            return {"response" : "move instance bad Response"}
        
        mid = create_move_instance(
            payload["game_instance_id"],
            payload["move"],
            payload["player"],             
            payload["prev_move_id"]
            ) 
        user_move = get_move_by_move_id(mid)
        return  moveview.single(user_move)