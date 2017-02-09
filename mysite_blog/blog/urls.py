
#Creating an urls.py file for each app is the best way to make your applications reusable by other projects
from django.conf.urls import url
from . import views

urlpatterns = [
    # post views
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
]
