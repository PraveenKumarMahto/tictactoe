from flask_restful import Resource,request
from validators.game_instance import validator
from dao.game_instance import create_game_instance
from views import game_instance as gameview

class GameInstance(Resource):
    def post(self):
        payload = request.json
        if not validator(payload):
            return {"response" : "game instance bad Response"}

        create_game_instance(payload["user1"],payload["user2"])    # bug
        return gameview.single(payload)

        
