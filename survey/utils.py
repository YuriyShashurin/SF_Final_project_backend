

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'username': user.username,
        'user_id' : user.id,
        'email' : user.email
    }
