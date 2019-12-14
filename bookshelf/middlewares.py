from django.contrib.auth import _get_user_session_key
from django.utils.deprecation import MiddlewareMixin


def get_profile_id(request):
    profile_id = None
    try:
        user_id = _get_user_session_key(request)
    except KeyError:
        pass
    else:
        from bookshelf import models

        profile_id = (
            models.Profile.objects.filter(user_id=user_id)
            .values_list("pk", flat=True)
            .first()
        )
    return profile_id


class ProfileIdMiddleware(MiddlewareMixin):
    def process_request(self, request):
        assert hasattr(request, "session")
        request.profile_id = get_profile_id(request)
