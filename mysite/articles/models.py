from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

# Create your models here.
def articles_image_path(instance, filename):
    return f'user_{instance.user.pk}/{filename}'

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    # blank = 유효성 검사시
    # null = DB 상의 컬럼의 Null
    # image = models.ImageField(blank=True, upload_to="%y/%m/%d/")
    image = models.ImageField(blank=True, upload_to=articles_image_path)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality':90}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_articles',
        blank=True
    )
    recommend = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="recommend_articles",
        blank=True
    )

    def __str__(self):
        return f'{self.pk}번째 글, {self.title}-{self.content}'

class Comment(models.Model):
    # 멤버 변수 = models.외래키(참조하는 객체, 삭제 되었을 때 처리 방법)
    article = models.ForeignKey(Article, on_delete=models.CASCADE) #, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 역참조 값 설정 related_name='comments'
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Article:{self.article}, {self.pk}-{self.content}'