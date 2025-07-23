from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from apps.common.models import BaseModel


# 사용자 관리자(Manager) 클래스 정의
# AbstractBaseUser를 사용할 때 필수적
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("이메일 주소는 필수입니다.")

        email = self.normalize_email(email)  # 이메일 주소를 정규화
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # 비밀번호 해싱
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # 관리자 생성 시 기본값 설정
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("슈퍼유저는 is_staff=True여야 합니다.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("슈퍼유저는 is_superuser=True여야 합니다.")

        return self.create_user(email, password, **extra_fields)


# 커스텀 User 모델 정의
# is_superuser, groups, user_permissions 필드는 PermissionsMixin이 제공
# has_perm, has_module_perms 등 메서드도 PermissionsMixin이 제공
class CustomUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    # 로그인 시 사용할 이메일 필드
    email = models.EmailField(
        verbose_name="이메일 주소",
        max_length=255,
        unique=True,
    )
    # 닉네임 필드
    nickname = models.CharField(max_length=50, unique=True, verbose_name="닉네임")
    # 이름 필드
    name = models.CharField(max_length=50, verbose_name="이름")
    # 전화번호 필드
    phone_number = models.CharField(
        max_length=15, blank=True, null=True, verbose_name="전화번호"
    )

    # 스태프 여부 (관리자 페이지 접근 권한)
    is_staff = models.BooleanField(default=False, verbose_name="스태프 여부")
    # 계정 활성화 여부
    is_active = models.BooleanField(default=True, verbose_name="계정 활성화 여부")

    # 사용자 식별을 위한 고유 필드 지정 (로그인 시 사용)
    USERNAME_FIELD = "email"
    # createsuperuser 명령 시 필수로 입력받을 필드 목록
    REQUIRED_FIELDS = ["nickname", "name"]

    # 커스텀 관리자 클래스를 objects로 연결
    objects = CustomUserManager()

    def __str__(self):
        # 사용자 객체를 문자열로 표현할 때 이메일 주소를 반환
        return self.email

    class Meta:
        verbose_name = "사용자"
        verbose_name_plural = "사용자들"

    