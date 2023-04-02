from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('video/',index , name="video"),
    path('video1/',index1 , name="video1"),
    path('video2/',index2 , name="video2"),
    path('',hom , name="home"),
    path('pay/',pay , name="pay"),
    path('paya/',paya , name="paya"),
    path('pay1/',pay1 , name="pay1"),
    path('paya1/',paya1 , name="paya1")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
