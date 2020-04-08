from django.urls import path
from . import views

#    path('', login_required(views.HomePageView.as_view()), name='home_page'),

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('list/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:year>/<int:month>/<int:day>/<str:slug>',
         views.post_detail, name='post_detail'),
    path('author/', views.AuthorPage.as_view(), name='author'),
    path('cat/', views.CatView.as_view(), name='kot'),
    path('basic_info/', views.send_basic_info, name='send_basic_info')
]
