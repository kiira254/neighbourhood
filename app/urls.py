from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path

urlpatterns=[
    path(r'',views.home,name='home'),
    re_path('new_profile/(?P<username>\w{0,50})',views.new_profile,name = 'new_profile'),
    path('search/',views.search,name='search'),
    re_path('post/(?P<id>\d+)',views.post,name='post'),
    path('business',views.Business,name = 'business'),
    path('api/business/',views.BusinessList.as_view())v

]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)