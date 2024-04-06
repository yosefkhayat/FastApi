from fastapi import APIRouter, HTTPException
from classes.auth_model import Sign_in_model as Sin,Sign_up_model as Sup
from db import auth_db_fns
from auth import auth_fns,jwt_handler
#router to Authentication
router = APIRouter(
    prefix = '/auth',
    tags = ['Authentication router']
)


@router.post('/sign_up')
def sign_up(body:Sup):
    if body.role != 'guest' and body.role != 'admin':
        raise HTTPException(status_code=400, detail="role must be guest or admin")
    try:
        auth_db_fns.find_user_in_db(body.username)
        raise HTTPException(status_code=400, detail="user exists")
    except FileNotFoundError:
        body = auth_fns.prepare_new_user_data(body)
        auth_db_fns.save_to_db(body)
        auth_token = jwt_handler.signJWT(body.username,body.role)
        return {"msg":"user created","token":auth_token}

@router.post('/sign_in')
def sign_in(body:Sin): 
    try:
        stored_user = auth_db_fns.find_user_in_db(body.username)
        if stored_user:
            stored_pass = stored_user["password"]
            if auth_fns.verify_password(stored_pass,body.password):
                auth_token = jwt_handler.signJWT(stored_user["username"],stored_user["role"])
                return {"msg":"user sign in successfully","token":auth_token}
            else:
                raise HTTPException(status_code=400, detail="invalid creds")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="no such username")