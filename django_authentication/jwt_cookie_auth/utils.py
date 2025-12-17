from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def set_auth_cookies(response, access, refresh=None):
    response.set_cookie(
        key='access',
        value=access,
        httponly=True,
        secure=True,
        samesite='Lax'
    )

    if refresh:
        response.set_cookie(
            key='refresh',
            value=refresh,
            httponly=True,
            secure=True,
            samesite='Strict'
        )
