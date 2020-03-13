from django.conf.urls import url
from django_opencv_app.views import ImageView, ImageListView, ImageAddView

app_name = 'django_opencv_app'

urlpatterns = [
    url(r'^edit/(?P<id>\d+)$', ImageView.as_view(), name='image-edit'),
    url(r'^$', ImageListView.as_view()),
    url(r'^add/', ImageAddView.as_view(), name='add-image'),
]