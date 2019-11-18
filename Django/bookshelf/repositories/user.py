from django.contrib.auth.models import User


def create_user(data):
    return User.objects.create(**data)


def save_password(user, raw_password):
    user.set_password(raw_password)
    user.save()
