from asyncio.windows_events import NULL
from email.policy import default
from pydoc import visiblename
from turtle import title
from django.db import models
from hashlib import md5
import uuid
from django.conf import settings

# Create your models here.
class Url(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name="Yazar")
    full_url=models.CharField(max_length=400)
    short_url=models.CharField(unique=True, max_length=20)
    created_date=models.DateTimeField(auto_now=True,verbose_name="oluşturma tarihi")
    url_show=models.BooleanField(default=True)
    deleted_date=models.DateTimeField(blank=True,null=True)
    click=models.PositiveIntegerField(default=1)
    subs= models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.full_url

    def save(self, **kwargs):
        self.short_url=uuid.uuid4().hex[:12].upper()
        super().save(**kwargs)
