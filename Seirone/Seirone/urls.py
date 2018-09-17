from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

#New apps place here
from profiles import views as profile_views
from contact import views as contact_views
#from my_photos import views as photos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', profile_views.home, name='home'),
    path('about-us/', profile_views.about, name='about'),
    path('profile/', profile_views.userProfile, name='profile'),
    path('contact/', contact_views.contact, name='contact'),
    path('cheat/', profile_views.cheat, name='cheat'),
    #path('photos/', include('my_photos.urls')),
    #path('photos/', photos_views.AlbumView, name='photos'),
    #path('<pk>/', photos_views.PictureView, name='pictures'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)