import base64
from django.db import models
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from cryptography.fernet import Fernet, InvalidToken

class EncryptedEmailField(models.EmailField):
    """
    A custom model field that automatically encrypts and decrypts
    email addresses using the Fernet symmetric encryption algorithm.
    """
    def __init__(self, *args, **kwargs):
        if not settings.ENCRYPTION_KEY:
            raise ImproperlyConfigured(
                "You must set the ENCRYPTION_KEY in your Django settings "
                "to use EncryptedEmailField."
            )
        # Create a Fernet instance with the key from settings
        self.fernet = Fernet(settings.ENCRYPTION_KEY.encode())
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        """
        Called to prepare the value for the database.
        This is where we encrypt the email.
        """
        if value is None:
            return value
        # Encrypt the string value and return the bytes
        return self.fernet.encrypt(value.encode('utf-8'))

    def from_db_value(self, value, expression, connection):
        """
        Called when data is loaded from the database.
        This is where we decrypt the email.
        """
        if value is None:
            return value
        try:
            # Decrypt the bytes and decode back to a string
            return self.fernet.decrypt(value).decode('utf-8')
        except InvalidToken:
            # If the token is invalid (e.g., not encrypted, wrong key),
            # return the original value. This helps with data migrations
            # from a plain text field.
            return value