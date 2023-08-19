from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.

#회원가입

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class MyAccountManager(BaseUserManager):
    # 일반 멤버
    def create_user(self, nickname, username, phonenum, birthY, birthM, birthD, password=None):
        if not nickname:
            raise ValueError("닉네임은 필수로 입력해야 합니다.")
        if not username:
            raise ValueError("이름은 필수로 입력해야 합니다.")
        if not phonenum:
            raise ValueError("전화번호는 필수로 입력해야 합니다.")
        if not birthY:
            raise ValueError("생일은 필수로 입력해야 합니다.")
        if not birthM:
            raise ValueError("생일은 필수로 입력해야 합니다.")
        if not birthD:
            raise ValueError("생일은 필수로 입력해야 합니다.")
        user = self.model(
            phonenum=phonenum,
            username=username,
            nickname = nickname,
            birthY = birthY,
            birthM = birthM,
            birthD = birthD,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자
    def create_superuser(self, nickname, username, phonenum, birthY, birthM, birthD, password):
        user = self.create_user(
            phonenum=phonenum,
            username=username,
            nickname=nickname,
            birthY=birthY,
            birthM=birthM,
            birthD=birthD,
            password=password,

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser, PermissionsMixin):
    nickname    = models.CharField(max_length=20, unique=True, null=False)
    username    = models.CharField(max_length=40, null=False, blank=False)
    phonenum    = models.IntegerField(unique=True)
    birthY      = IntegerRangeField(max_value=3000)
    birthM      = IntegerRangeField(max_value=12)
    birthD      = IntegerRangeField(max_value=32)
    create_at   = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login  = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    favorite_products = models.ManyToManyField('shop.Product', related_name='favorite_products', blank=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'phonenum'
    REQUIRED_FIELDS = ['username', 'nickname', 'birthY', 'birthM', 'birthD']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lable):
        return True

