from django.conf.urls import url


from .views import index, results, detail, vote, add_poll

app_name = 'polls'

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^(?P<question_id>[0-9]+)$', detail, name="detail"),
    url(r'^(?P<question_id>[0-9]+)/results/$',
        results, name="results"),
    url(r'^(?P<question_id>[0-9]+)/vote/$', vote, name="vote"),
    url(r'^add/$', add_poll, name="add_poll")
]
