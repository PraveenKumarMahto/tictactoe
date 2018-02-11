
def single(move_object):
    return {
        "move_id" : str(move_object.get("_id",))
        "game_instance_id" : str(move_object["game_instance_id"]),
        "move_id" : move_object.get("move_id","No Email Address"),
        "player" : move_object.get("player","Default Name"),
        "previous_move_id" : move_object.get("prev_move_id", "None") 
    }

def multiple(user_objects):
    return [ single(user_object) for user_object in user_objects ]