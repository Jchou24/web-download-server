# Manually generate
from django.conf.urls import patterns, url
from downloader import views

# ==================================
# hard version
# urlpatterns = patterns('',
#     # ex: /polls/
#     url(r'^$', views.index, name='index'),
#     # ex: /polls/5/
#     url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
#     # ex: /polls/5/vote/
#     url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
# )

# ==================================
# simple version with generic view
urlpatterns = patterns('',
    url(r'^download/$', views.download, name='download'),
    url(r'^pull/$', views.pull, name='pull'),
)
