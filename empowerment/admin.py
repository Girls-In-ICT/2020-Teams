from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from empowerment.models import UserProfile, LibraryBook, BookComment, Video, VideoComment

admin.site.register(UserProfile)
admin.site.register(LibraryBook)
admin.site.register(BookComment)
admin.site.register(Video)
admin.site.register(VideoComment)

