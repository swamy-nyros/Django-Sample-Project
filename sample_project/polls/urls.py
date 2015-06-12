from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.IndexView.as_view(), name='index'),    
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/comment/$', views.comment, name='comment'),
    url(r'^(?P<question_id>[0-9]+)/post_comment/$', views.post_comment, name='post_comment'),
    url(r'^file_upload/$', views.file_upload, name='file_upload'),   
    
    
]