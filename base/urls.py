from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'base'

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery', views.gallery, name='gallery'),
    path('news', views.news, name='news'),
    path('top_students', views.top_students_page, name='top_students'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('about_school', views.about_school, name='about_school')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
