from jsonschema import validate

schema = {
            "type" : "object",
            "properties" : {
                "user1" : {"type" : "string"},
                "user2" : {"type" : "string"}
            }
        }

def validator(payload):
    try:
        validate(payload,schema)
        return True
    except:
        return False