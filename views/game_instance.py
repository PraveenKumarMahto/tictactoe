

def single(game_instance_object):
    return {
        "user1" : game_instance_object.get("user1","Default user1"),
        "user2" : game_instance_object.get("user2","Default user2"),
        "curr_status" : game_instance_object.get("curr_status","default state"),
        "next_player" : game_instance_object.get("next_player","default user1"),
        "status" : game_instance_object.get("status","default game status"),
        "winner" : game_instance_object.get("winner","None"),
        "curr_move_id" : game_instance_object.get("curr_move_id","None")
    }

def multiple(game_instance_objects):
    return [ single(game_instance_object) for game_instance_object in game_instance_objects ]