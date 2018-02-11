from jsonschema import validate

schema = {
            "type" : "object",
            "properties" : {
                "game_instance_id" : {"type" : "string"},
                "move" : {"type" : "string"},
                "player" : {"type" : "string"},
                "prev_move_id" : {"type" : "string"}
            }
        }

def validator(payload):
    try:
        validate(payload,schema)
        return True
    except:
        return False
