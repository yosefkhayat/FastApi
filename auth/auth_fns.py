import bcrypt
import sys
import os
# Remove these two lines after finishing the development of thid module
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from classes.auth_model import Sign_up_model,Sign_in_model

def hash_password(password: str) -> str:
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')


def verify_password(stored_pass,user_pass):
    return bcrypt.checkpw(user_pass.encode('utf-8'), stored_pass.encode('utf-8'))

def prepare_new_user_data(user:Sign_up_model):
    user.password = hash_password(user.password)
    return user
