__version__ = '__VERSION__'
__all__ = (
    'TOTP',
    'generate_random_base32_secret',
)

from .otp import TOTP, generate_random_base32_secret
