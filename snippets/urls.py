from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^snippets/$', view=views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', view=views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)