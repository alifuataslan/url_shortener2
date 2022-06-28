from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# FIXME choices de 1234 değil onları bir değişkene atayıp onları kullanmalısın çünkü eğer değer değişir ise aldın başına belayıııı
class User(AbstractUser):
    subs= models.BooleanField(default=False)
    sub_type=models.PositiveBigIntegerField(choices=[(1,"Free"),(2,"silver"),(3,"Gold"),(4,"Premium")],default=1)
