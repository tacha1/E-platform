from django.conf.urls import url
from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home_page,name = 'home'),
    url('^single_service/(\d+)/$',views.view_service,name = 'single_service'),
    url(r'^new/profile$', views.add_profile, name='edit'),
    url(r'^myprofile$', views.my_profile, name='myprofile'),
    url(r'^all_users/$', views.all_users, name='all_users'),
    url('^single_user/(\d+)/$',views.one_user,name = 'single_user')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)