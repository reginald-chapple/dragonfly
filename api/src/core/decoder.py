import os
from cryptography.fernet import Fernet, InvalidToken
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def decrypt_value(encrypted_value: bytes) -> str:
    """
    Decrypts a value using the key from the environment.
    """
    # 1. Get the key from the environment
    key = os.environ.get('ENCRYPTION_KEY')
    if not key:
        raise ValueError("ENCRYPTION_KEY not found in environment variables.")

    # 2. Initialize Fernet with the key
    fernet = Fernet(key.encode())

    # 3. Decrypt the value
    try:
        decrypted_bytes = fernet.decrypt(encrypted_value)
        # 4. Decode from bytes to a human-readable string
        return decrypted_bytes.decode('utf-8')
    except InvalidToken:
        return "Decryption failed: The token is invalid or the key is wrong."
    except Exception as e:
        return f"An error occurred: {e}"