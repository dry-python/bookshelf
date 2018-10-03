from attr import attrib, attrs
from django.contrib.auth import login, password_validation
from django.core.exceptions import ValidationError


def validate_password(raw_password):

    try:
        password_validation.validate_password(raw_password)
    except ValidationError as error:
        return False, error
    else:
        return True, None


@attrs
class StoreUserInSession:

    request = attrib()

    def do(self, user):

        login(self.request, user)
