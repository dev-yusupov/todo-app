import jwt
import time

def create_jwt_token(user):
    """Create JSON Web Token for user"""

    payload = {
        'sub': user.id,
        'exp': time.time() + 60 * 60,
    }
    
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    return token