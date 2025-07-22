from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="데이터 생성 일시"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="최근 업데이트 일시")

    class Meta:
        abstract = True