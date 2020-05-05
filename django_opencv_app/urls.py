from django.conf.urls import url
from django_opencv_app.views import IndexView, CreateImageView, EditCv2ImageView


app_name = 'django_opencv_app'

urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
    url(r'^add/', CreateImageView, name='image_add'),
    url(r'^edit/(?P<id>\d+)$', EditCv2ImageView, name='image_edit'),
]