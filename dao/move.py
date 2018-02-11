from pymongo import MongoClient
from bson import ObjectId

client = MongoClient()
db = client.game_engine

movectln = db.moves

def create_move_instance(game_instance_id , prev_move_id , move, player ):
    mid = movectln.insert_one(
            { "game_instance_id" : game_instance_id,
               "prev_move_id" : prev_move_id,
               "move" : move,
               "player" : player
            }
    )
    return mid

#def get_move_by_game_id(game_id):
#   return movectln.find({"game_instance_id" : game_id})
    

