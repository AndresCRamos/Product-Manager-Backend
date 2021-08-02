from datetime import timedelta
from django.utils import timezone
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .settings import TOKEN_EXPIRED_AFTER_SECONDS


def expires_in(token):
    time_elapsed = timezone.now() - token.created
    left_time = timedelta(seconds=TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
    return left_time


# token checker if token expired or not
def is_token_expired(token):
    return expires_in(token) < timedelta(seconds=0)


class ExpiringTokenAuthentication(TokenAuthentication):
    """
    If token is expired then it will be removed
    and new one with different key will be created
    """

    def token_expire_handler(self, token):
        is_expired = is_token_expired(token)
        return is_expired, token

    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Invalid Token")

        if not token.user.is_active:
            raise AuthenticationFailed("User is not active")

        is_expired, token = self.token_expire_handler(token)

        if is_expired:
            raise AuthenticationFailed("The Token is expired")

        return token.user, token
