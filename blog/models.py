from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# Post가 장고 모델임을 의미하며, 이 코드 때문에, 장고는 Post가 데이터베이스에 저장되어야 된다고 알게 됨.
class Post(models.Model):
    # foreign key로 선언...
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 제목 필드의 총 길이는 200 
    title = models.CharField(max_length=200)
    # 글자 수 제한이 없는 Textfield
    text = models.TextField()
    # 글을 쓴 날짜는 timezone의 현재 시간을 반영
    create_date = models.DateTimeField(
        default=timezone.now
    )
    # 수정한 날짜
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
