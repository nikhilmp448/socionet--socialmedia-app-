from django.contrib import admin

from fgroups.models import Groups,Group_members

# Register your models here.
admin.site.register(Groups)
admin.site.register(Group_members)