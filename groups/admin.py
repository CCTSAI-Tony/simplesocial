from django.contrib import admin
from . import models

# Register your models here. allow to utilize the admin interface to edit model in the same page as a parent model
# like GroupMember is belonging to Group model
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)

# Register your models here.
