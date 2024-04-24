from django.contrib import admin
from discussion.models import Discussion, DiscussionComment


# Register your models here.

admin.site.register((DiscussionComment))
admin.site.register((Discussion))