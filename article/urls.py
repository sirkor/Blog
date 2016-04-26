from django.conf.urls import url, patterns, include


urlpatterns = [

    url(r'^articles/all/$', 'article.views.articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^$', 'article.views.articles'),
]
