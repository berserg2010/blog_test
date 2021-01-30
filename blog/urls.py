from django.urls import path

from .views import index, new_article, detail_article


app_name = 'blog'

urlpatterns = [
    path('', index, name='list_articles'),

    path('detail_article/<int:article_id>/', detail_article, name='detail_article'),

    path('new_article/', new_article, name='new_article'),
]
