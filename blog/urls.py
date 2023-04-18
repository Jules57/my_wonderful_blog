from django.urls import path
from .views import add_comment, show_blog, show_about, show_article, create_article, update_article, delete_article
from .views import show_profile, change_password, register, login, logout

urlpatterns = [
    path('', show_blog, name='home'),
    path('blogs/', show_blog, name='blogs'),
    path('about/', show_about, name='about'),
    path('create/', create_article, name='create_article'),
    path('profile/<str:username>/', show_profile, name='show_profile'),
    path('change_password/', change_password, name='change_password'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('<slug:article_slug>/', show_article),
    path('<slug:article_slug>/comment/', add_comment, name='add_comment'),
    path('<slug:article_slug>/update/', update_article, name='update_article'),
    path('<slug:article_slug>/delete/', delete_article, name='delete_article'),
]
