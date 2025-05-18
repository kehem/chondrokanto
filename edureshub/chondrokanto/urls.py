
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('blog',views.my_blog, name='blog'),
    path('blogview/<id>',views.blogview, name='blogview'),
    path('category/<id>',views.my_category, name='category'),
    path('videos/<id>',views.videos, name='videos'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('info',views.information, name='info'),
    path('blog_dashboard',views.blog_dashboard, name='blog_dashboard'),
    path('blog_dashboard_edit/<id>',views.blog_dashboard_edit, name='blog_dashboard_edit'),
    path('category_dashboard',views.category_dashboard, name='category_dashboard'),
    path('category_dashboard_edit/<id>',views.category_dashboard_edit, name='category_dashboard_edit'),
    path('album_dashboard',views.album_dashboard, name='album_dashboard'),
    path('album_dashboard_edit/<id>',views.album_dashboard_edit, name='album_dashboard_edit'),
    path('video_dashboard',views.video_dashboard, name='video_dashboard'),
    path('video_dashboard_edit/<id>',views.video_dashboard_edit, name='video_dashboard_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)