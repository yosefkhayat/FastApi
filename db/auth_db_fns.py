import json
from classes import auth_model as user


def load_data_from_json(file_location = 'db/auth_db.json'):
    try:
        with open(file_location,"r") as f:
            data= json.load(f)
    except json.JSONDecodeError as e:
        print("Invalid JSON syntax:", e)
        data = {}
    except FileNotFoundError as e:
        with open(file_location,"x") as f:
            json.dump({},f)
            f.flush()
            data =json.load(f)
    return data

def update_data(body:user.Sign_up_model):
    db = load_data_from_json()
    db[body.username] = {
        "fullname":body.fullname,
        "username": body.username,
        "password": body.password,
        "role": body.role
    }
    return db

def save_to_db(body:user.Sign_up_model):
    updated_db=update_data(body)
    with open('db/auth_db.json','w') as f:
        f.write(json.dumps(updated_db))
        f.close()
        
def find_user_in_db(username):
    db = load_data_from_json("db/auth_db.json")
    if username in db:
        return db[username]
    else:
        raise FileNotFoundError(f'username: {username} not in db')
    