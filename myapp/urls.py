from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('about/',views.about,name='about'),
    path('detail/',views.detail, name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


