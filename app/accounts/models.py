from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('must have user email')
        
        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True) #이에밀
    name = models.CharField(default='', max_length=100, null=False, blank=False) #사용자 성함
    department = models.CharField(default='', max_length=100, null=True, blank=True) #학과
    studentid = models.CharField(default='', max_length=100, null=True, blank=True) #학번
    schoolcertification = models.BooleanField(default = False) #학교인증 여부
    
    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    
    # 헬퍼 클래스 사용
    objects = UserManager()

    # 필수로 작성해야하는 field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name