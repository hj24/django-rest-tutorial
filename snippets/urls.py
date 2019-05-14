from django.conf.urls import url, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url('^$', views.api_root),
    url(r'^snippets/$', view=views.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', view=views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', view=views.SnippetHighlight.as_view(), name='snippet-highlight'),
    url(r'^users/$', view=views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', view=views.UserDetail.as_view(), name='user-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
