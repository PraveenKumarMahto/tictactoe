from flask_restful import Resource,request
from validators.game_instance import validator
from dao.game_instance import create_game_instance,get_game_instance,get_all_game_instances
from views import game_instance as gameview
from bson import ObjectId


class GameInstance(Resource):
    def get(self,game_instance_id = None):
        if game_instance_id:
            game_id = get_game_instance(ObjectId(game_instance_id))
        
            if not game_id :
                return { 'response' : 'Game_instance_id not found'} , 404
            return { 'response' : gameview.single(game_id) } ,200

        game_ids = get_all_game_instances()
        return { 'response' : gameview.multiple(game_ids)}       



    def post(self):
        payload = request.json
        if not validator(payload):
            return {"response" : "game instance bad Response"}

        create_game_instance(payload["user1"],payload["user2"])    # bug
        return gameview.single(payload)

        
if __name__=="__main__":
    gi = GameInstance()
    print gi.get()