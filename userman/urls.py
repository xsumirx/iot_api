from django.conf.urls import url,include
from . import views

urlpatterns = [
	url(r'^create/$',views.create_user, name='create_new_user'),
]