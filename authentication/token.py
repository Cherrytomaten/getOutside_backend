import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        print('generate token:')
        token = six.text_type(user.id) + six.text_type(timestamp) + six.text_type(user.is_active)
        print(token)
        return token


account_activation_token = TokenGenerator()
