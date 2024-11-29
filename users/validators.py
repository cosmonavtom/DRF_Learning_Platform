import re
from django.core.validators import ValidationError


class PasswordValidator:
    ''' Непосредственно валидатор паролей '''
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg_pattern = re.compile(r'^[a-zA-Z0-9]+$')
        tmp_value = dict(value).get(self.field)
        if not bool(reg_pattern.match(tmp_value)):
            raise ValidationError('Пароль должен содержать только латинские буквы и цифры')