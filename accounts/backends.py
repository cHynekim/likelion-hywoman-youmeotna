from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class CaseInsensitiveModelBackend(ModelBackend):
    def authenticate(self, request, phonenum=None, password=None, **kwargs):
        UserModel = get_user_model()
        if phonenum is None:
            phonenum = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            case_insensitive_phonenum_field = '{}__iexact'.format(UserModel.USERNAME_FIELD)
            user = UserModel._default_manager.get(**{case_insensitive_phonenum_field: phonenum})
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user