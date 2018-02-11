

def single(game_instance_object):
    return {
        "user1" : str(game_instance_object.get("user1","Default user1")),
        "user2" : str(game_instance_object.get("user2","Default user2")),
        "curr_status" : game_instance_object.get("curr_status","default state"),
        "next_player" : str(game_instance_object.get("next_player","default user1")),
        "status" : game_instance_object.get("status","default game status"),
        "winner" : str(game_instance_object.get("winner","None")),
        "curr_move_id" : str(game_instance_object.get("curr_move_id","None"))
    }

def multiple(game_instance_objects):
    return [ single(game_instance_object) for game_instance_object in game_instance_objects ]