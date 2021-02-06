from flask_login import current_user

def username():
    return current_user.username