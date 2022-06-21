from django.contrib import admin
from user.models import User
from user.models import UserProfile
from user.models import Hobby

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Hobby)