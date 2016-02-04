from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    likes_cheese = models.BooleanField()

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
