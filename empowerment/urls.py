from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from empowerment import views

urlpatterns = [
                  path('', views.home, name='home'),
                  path('register/', views.register, name='register'),
                  path('main/', views.mainPage, name='main'),
                  path('logout/', views.logout_view, name='logout'),
                  path('library/', views.library, name='library'),
                  path('video/', views.video, name='video'),
                  path('comment/<libraryId>', views.comment, name='comment'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
