# Core Django imports.
from django.urls import path

# Blog application imports.
from blog.views.blog_views import (
    ArticleListView,
    CategoryArticleListView,
    AuthorArticleListView,
    CategoriesListView,
    AuthorsListView,
    ArticleDetailView,
    ArticleSearchListView,
    ArticleCreateView,
)

# Specifies the app name for name spacing.
app_name = "blog"

# blog/urls.py
urlpatterns = [
    # /home/
    path('', ArticleListView.as_view(), name='home'),

    # category-articles/<str:slug>/
    path('category-articles/<str:slug>/', CategoryArticleListView.as_view(),
         name='category_articles'
         ),

    # /author/<str:username>/
    path('author-articles/<str:username>/', AuthorArticleListView.as_view(),
         name='author_articles'
         ),

    # /categories-list/
    path('categories-list/', CategoriesListView.as_view(),
         name='categories_list'
         ),

    # /authors-list/
    path('authors-list/', AuthorsListView.as_view(), name='authors_list'),

    # /article/<str:slug>/
    path('article/<str:slug>/', ArticleDetailView.as_view(),
         name='article_detail'
         ),

    # /search/?q=query/
    path('search/', ArticleSearchListView.as_view(),
         name='article_search_list_view'
         ),

    # /article/new/
    path('article-new/', ArticleCreateView.as_view(),
         name="article_create")

]
