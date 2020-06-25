from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="followings",
        blank=True
    )
    # 각족 필드들 추가
    # createsuperuser 불가 따라서 필드 추가하기 전에 admin 계정 만드는 것이 좋다.
    # shell_plus
    # create_user is_staff, is_superuser True