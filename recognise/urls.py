from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$' , views.process_image , name="process_image") ,

]