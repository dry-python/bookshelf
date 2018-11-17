from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError


def validate_password(raw_password):

    try:
        password_validation.validate_password(raw_password)
    except ValidationError as error:
        return False, error
    else:
        return True, None
